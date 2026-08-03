from __future__ import annotations

import asyncio
import json
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, AsyncIterator, Callable

from fastapi import WebSocket

from app.other.settings import settings
from app.other.types import EventKind, SimEvent

try:
    import redis.asyncio as redis
except Exception:
    redis = None


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class EventFilter:
    kinds: set[EventKind] = field(default_factory=set)
    min_tick: int = 0
    flight_id: str = ""
    runway_id: str = ""
    gate_id: str = ""
    text: str = ""

    def match(self, item: SimEvent) -> bool:
        if self.kinds and item.kind not in self.kinds:
            return False
        if item.tick < self.min_tick:
            return False
        if self.flight_id and item.data.get("flight_id") != self.flight_id:
            return False
        if self.runway_id and item.data.get("runway_id") != self.runway_id:
            return False
        if self.gate_id and item.data.get("gate_id") != self.gate_id:
            return False
        if self.text and self.text.lower() not in item.text.lower():
            return False
        return True

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> EventFilter:
        kinds = set()
        for val in data.get("kinds", []):
            try:
                kinds.add(EventKind(val))
            except ValueError:
                pass
        return cls(
            kinds=kinds,
            min_tick=int(data.get("min_tick", 0)),
            flight_id=str(data.get("flight_id", "")),
            runway_id=str(data.get("runway_id", "")),
            gate_id=str(data.get("gate_id", "")),
            text=str(data.get("text", "")),
        )


class WebSocketHub:
    def __init__(self) -> None:
        self.items: dict[str, set[WebSocket]] = defaultdict(set)
        self.filters: dict[int, EventFilter] = {}
        self.lock = asyncio.Lock()
        self.sent = 0
        self.failed = 0

    async def connect(self, sim_id: str, ws: WebSocket) -> None:
        await ws.accept()
        async with self.lock:
            self.items[sim_id].add(ws)
            self.filters[id(ws)] = EventFilter()
        await self.send_one(ws, {"kind": "connected", "sim_id": sim_id, "time": now_text()})

    async def disconnect(self, sim_id: str, ws: WebSocket) -> None:
        async with self.lock:
            if sim_id in self.items:
                self.items[sim_id].discard(ws)
                if not self.items[sim_id]:
                    self.items.pop(sim_id, None)
            self.filters.pop(id(ws), None)

    async def set_filter(self, ws: WebSocket, data: dict[str, Any]) -> None:
        async with self.lock:
            self.filters[id(ws)] = EventFilter.from_data(data)

    async def send_one(self, ws: WebSocket, data: dict[str, Any]) -> bool:
        try:
            await ws.send_json(data)
            self.sent += 1
            return True
        except Exception:
            self.failed += 1
            return False

    async def send_text(self, ws: WebSocket, text: str) -> bool:
        try:
            await ws.send_text(text)
            self.sent += 1
            return True
        except Exception:
            self.failed += 1
            return False

    async def broadcast(self, sim_id: str, item: SimEvent) -> int:
        async with self.lock:
            vals = list(self.items.get(sim_id, set()))
            filters = {id(x): self.filters.get(id(x), EventFilter()) for x in vals}
        good = 0
        bad = []
        data = item.to_dict()
        for ws in vals:
            check = filters[id(ws)]
            if not check.match(item):
                continue
            if await self.send_one(ws, data):
                good += 1
            else:
                bad.append(ws)
        for ws in bad:
            await self.disconnect(sim_id, ws)
        return good

    async def broadcast_data(self, sim_id: str, data: dict[str, Any]) -> int:
        async with self.lock:
            vals = list(self.items.get(sim_id, set()))
        good = 0
        bad = []
        for ws in vals:
            if await self.send_one(ws, data):
                good += 1
            else:
                bad.append(ws)
        for ws in bad:
            await self.disconnect(sim_id, ws)
        return good

    def count(self, sim_id: str | None = None) -> int:
        if sim_id is not None:
            return len(self.items.get(sim_id, set()))
        return sum(len(x) for x in self.items.values())

    def stats(self) -> dict[str, Any]:
        return {
            "connections": self.count(),
            "simulations": len(self.items),
            "sent": self.sent,
            "failed": self.failed,
            "by_simulation": {k: len(v) for k, v in self.items.items()},
        }

    async def ping_all(self) -> int:
        async with self.lock:
            vals = [(key, ws) for key, group in self.items.items() for ws in group]
        good = 0
        for sim_id, ws in vals:
            if await self.send_one(ws, {"kind": "ping", "sim_id": sim_id, "time": now_text()}):
                good += 1
        return good

    async def close_sim(self, sim_id: str) -> int:
        async with self.lock:
            vals = list(self.items.get(sim_id, set()))
        count = 0
        for ws in vals:
            try:
                await ws.close()
                count += 1
            except Exception:
                pass
            await self.disconnect(sim_id, ws)
        return count

    async def close_all(self) -> int:
        async with self.lock:
            ids = list(self.items.keys())
        total = 0
        for sim_id in ids:
            total += await self.close_sim(sim_id)
        return total


class EventBus:
    def __init__(self, hub: WebSocketHub | None = None) -> None:
        self.hub = hub or WebSocketHub()
        self.listeners: list[Callable[[SimEvent], Any]] = []
        self.items: dict[str, deque[SimEvent]] = defaultdict(lambda: deque(maxlen=settings.max_events_per_sim))
        self.queues: dict[str, set[asyncio.Queue[SimEvent]]] = defaultdict(set)
        self.redis = None
        self.redis_ok = False
        self.published = 0
        self.listener_errors = 0

    async def start(self) -> bool:
        if not settings.use_redis or redis is None:
            return False
        try:
            self.redis = redis.from_url(settings.redis_url, decode_responses=True)
            await self.redis.ping()
            self.redis_ok = True
            return True
        except Exception:
            self.redis = None
            self.redis_ok = False
            return False

    async def stop(self) -> None:
        if self.redis is not None:
            try:
                await self.redis.close()
            except Exception:
                pass
        self.redis = None
        self.redis_ok = False

    def add_listener(self, fn: Callable[[SimEvent], Any]) -> None:
        if fn not in self.listeners:
            self.listeners.append(fn)

    def remove_listener(self, fn: Callable[[SimEvent], Any]) -> None:
        if fn in self.listeners:
            self.listeners.remove(fn)

    async def publish(self, item: SimEvent) -> SimEvent:
        self.items[item.sim_id].append(item)
        self.published += 1
        for fn in list(self.listeners):
            try:
                out = fn(item)
                if asyncio.iscoroutine(out):
                    await out
            except Exception:
                self.listener_errors += 1
        for q in list(self.queues.get(item.sim_id, set())):
            try:
                q.put_nowait(item)
            except asyncio.QueueFull:
                try:
                    q.get_nowait()
                    q.put_nowait(item)
                except Exception:
                    pass
        if self.redis_ok and self.redis is not None:
            try:
                await self.redis.publish(f"sim:{item.sim_id}:events", json.dumps(item.to_dict()))
            except Exception:
                self.redis_ok = False
        await self.hub.broadcast(item.sim_id, item)
        return item

    async def make(self, sim_id: str, tick: int, kind: EventKind, text: str, data: dict[str, Any] | None = None) -> SimEvent:
        item = SimEvent.make(sim_id, tick, kind, text, data)
        await self.publish(item)
        return item

    def recent(self, sim_id: str, limit: int = 100, event_filter: EventFilter | None = None) -> list[SimEvent]:
        vals = list(self.items.get(sim_id, deque()))
        if event_filter is not None:
            vals = [x for x in vals if event_filter.match(x)]
        if limit > 0:
            vals = vals[-limit:]
        return vals

    def clear(self, sim_id: str) -> int:
        count = len(self.items.get(sim_id, deque()))
        self.items.pop(sim_id, None)
        return count

    def clear_all(self) -> int:
        count = sum(len(x) for x in self.items.values())
        self.items.clear()
        return count

    async def stream(self, sim_id: str, size: int = 100) -> AsyncIterator[SimEvent]:
        q: asyncio.Queue[SimEvent] = asyncio.Queue(maxsize=size)
        self.queues[sim_id].add(q)
        try:
            while True:
                item = await q.get()
                yield item
        finally:
            self.queues[sim_id].discard(q)
            if not self.queues[sim_id]:
                self.queues.pop(sim_id, None)

    async def replay(self, sim_id: str, ws: WebSocket, limit: int = 100) -> int:
        vals = self.recent(sim_id, limit=limit)
        count = 0
        for item in vals:
            if await self.hub.send_one(ws, item.to_dict()):
                count += 1
        return count

    def counts(self, sim_id: str) -> dict[str, int]:
        out: dict[str, int] = {}
        for item in self.items.get(sim_id, deque()):
            key = item.kind.value
            out[key] = out.get(key, 0) + 1
        return out

    def flight_events(self, sim_id: str, flight_id: str, limit: int = 1000) -> list[SimEvent]:
        fil = EventFilter(flight_id=flight_id)
        return self.recent(sim_id, limit=limit, event_filter=fil)

    def runway_events(self, sim_id: str, runway_id: str, limit: int = 1000) -> list[SimEvent]:
        fil = EventFilter(runway_id=runway_id)
        return self.recent(sim_id, limit=limit, event_filter=fil)

    def gate_events(self, sim_id: str, gate_id: str, limit: int = 1000) -> list[SimEvent]:
        fil = EventFilter(gate_id=gate_id)
        return self.recent(sim_id, limit=limit, event_filter=fil)

    def stats(self) -> dict[str, Any]:
        return {
            "published": self.published,
            "listener_errors": self.listener_errors,
            "redis_ok": self.redis_ok,
            "simulations": len(self.items),
            "events": sum(len(x) for x in self.items.values()),
            "queues": sum(len(x) for x in self.queues.values()),
            "websockets": self.hub.stats(),
        }


hub = WebSocketHub()
bus = EventBus(hub)
