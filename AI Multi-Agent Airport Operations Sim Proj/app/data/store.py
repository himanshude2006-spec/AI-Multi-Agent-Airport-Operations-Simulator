from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.other.settings import settings
from app.other.types import Experiment, SimState

try:
    import redis.asyncio as redis
except Exception:
    redis = None


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


class MemoryStore:
    def __init__(self) -> None:
        self.sims: dict[str, SimState] = {}
        self.experiments: dict[str, Experiment] = {}
        self.values: dict[str, Any] = {}
        self.times: dict[str, str] = {}
        self.lock = asyncio.Lock()
        self.reads = 0
        self.writes = 0
        self.deletes = 0

    async def save_sim(self, state: SimState) -> SimState:
        async with self.lock:
            self.sims[state.id] = state.copy()
            self.times[f"sim:{state.id}"] = now_text()
            self.writes += 1
        return state

    async def get_sim(self, sim_id: str) -> SimState | None:
        async with self.lock:
            item = self.sims.get(sim_id)
            self.reads += 1
            return item.copy() if item is not None else None

    async def delete_sim(self, sim_id: str) -> bool:
        async with self.lock:
            item = self.sims.pop(sim_id, None)
            self.times.pop(f"sim:{sim_id}", None)
            self.deletes += 1
            return item is not None

    async def list_sims(self) -> list[SimState]:
        async with self.lock:
            vals = [x.copy() for x in self.sims.values()]
            self.reads += 1
        vals.sort(key=lambda x: x.updated_at, reverse=True)
        return vals

    async def save_experiment(self, item: Experiment) -> Experiment:
        async with self.lock:
            self.experiments[item.id] = item.copy()
            self.times[f"exp:{item.id}"] = now_text()
            self.writes += 1
        return item

    async def get_experiment(self, experiment_id: str) -> Experiment | None:
        async with self.lock:
            item = self.experiments.get(experiment_id)
            self.reads += 1
            return item.copy() if item is not None else None

    async def delete_experiment(self, experiment_id: str) -> bool:
        async with self.lock:
            item = self.experiments.pop(experiment_id, None)
            self.times.pop(f"exp:{experiment_id}", None)
            self.deletes += 1
            return item is not None

    async def list_experiments(self) -> list[Experiment]:
        async with self.lock:
            vals = [x.copy() for x in self.experiments.values()]
            self.reads += 1
        vals.sort(key=lambda x: x.updated_at, reverse=True)
        return vals

    async def set_value(self, key: str, value: Any) -> Any:
        async with self.lock:
            self.values[key] = value
            self.times[f"val:{key}"] = now_text()
            self.writes += 1
        return value

    async def get_value(self, key: str, default: Any = None) -> Any:
        async with self.lock:
            self.reads += 1
            return self.values.get(key, default)

    async def delete_value(self, key: str) -> bool:
        async with self.lock:
            item = self.values.pop(key, None)
            self.times.pop(f"val:{key}", None)
            self.deletes += 1
            return item is not None

    async def clear(self) -> dict[str, int]:
        async with self.lock:
            out = {"sims": len(self.sims), "experiments": len(self.experiments), "values": len(self.values)}
            self.sims.clear()
            self.experiments.clear()
            self.values.clear()
            self.times.clear()
            return out

    def stats(self) -> dict[str, Any]:
        return {
            "kind": "memory",
            "sims": len(self.sims),
            "experiments": len(self.experiments),
            "values": len(self.values),
            "reads": self.reads,
            "writes": self.writes,
            "deletes": self.deletes,
        }


class RedisStore:
    def __init__(self, url: str | None = None) -> None:
        self.url = url or settings.redis_url
        self.client = None
        self.ok = False
        self.reads = 0
        self.writes = 0
        self.errors = 0

    async def start(self) -> bool:
        if redis is None or not settings.use_redis:
            self.ok = False
            return False
        try:
            self.client = redis.from_url(self.url, decode_responses=True)
            await self.client.ping()
            self.ok = True
            return True
        except Exception:
            self.client = None
            self.ok = False
            self.errors += 1
            return False

    async def stop(self) -> None:
        if self.client is not None:
            try:
                await self.client.close()
            except Exception:
                self.errors += 1
        self.client = None
        self.ok = False

    async def save_sim(self, state: SimState) -> bool:
        if not self.ok or self.client is None:
            return False
        try:
            key = f"airport:sim:{state.id}"
            await self.client.set(key, state.json(), ex=settings.cache_seconds)
            await self.client.zadd("airport:sims", {state.id: float(state.tick)})
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            self.ok = False
            return False

    async def get_sim(self, sim_id: str) -> SimState | None:
        if not self.ok or self.client is None:
            return None
        try:
            text = await self.client.get(f"airport:sim:{sim_id}")
            self.reads += 1
            return SimState.from_json(text) if text else None
        except Exception:
            self.errors += 1
            self.ok = False
            return None

    async def delete_sim(self, sim_id: str) -> bool:
        if not self.ok or self.client is None:
            return False
        try:
            count = await self.client.delete(f"airport:sim:{sim_id}")
            await self.client.zrem("airport:sims", sim_id)
            self.writes += 1
            return bool(count)
        except Exception:
            self.errors += 1
            self.ok = False
            return False

    async def list_sim_ids(self, limit: int = 100) -> list[str]:
        if not self.ok or self.client is None:
            return []
        try:
            vals = await self.client.zrevrange("airport:sims", 0, max(0, limit - 1))
            self.reads += 1
            return list(vals)
        except Exception:
            self.errors += 1
            self.ok = False
            return []

    async def save_experiment(self, item: Experiment) -> bool:
        if not self.ok or self.client is None:
            return False
        try:
            key = f"airport:exp:{item.id}"
            await self.client.set(key, json.dumps(item.to_dict(), separators=(",", ":")), ex=settings.cache_seconds)
            await self.client.zadd("airport:experiments", {item.id: float(len(item.items))})
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            self.ok = False
            return False

    async def get_experiment(self, experiment_id: str) -> Experiment | None:
        if not self.ok or self.client is None:
            return None
        try:
            text = await self.client.get(f"airport:exp:{experiment_id}")
            self.reads += 1
            return Experiment.from_dict(json.loads(text)) if text else None
        except Exception:
            self.errors += 1
            self.ok = False
            return None

    async def set_value(self, key: str, value: Any, seconds: int | None = None) -> bool:
        if not self.ok or self.client is None:
            return False
        try:
            text = json.dumps(value, default=str, separators=(",", ":"))
            await self.client.set(f"airport:value:{key}", text, ex=seconds or settings.cache_seconds)
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            self.ok = False
            return False

    async def get_value(self, key: str, default: Any = None) -> Any:
        if not self.ok or self.client is None:
            return default
        try:
            text = await self.client.get(f"airport:value:{key}")
            self.reads += 1
            return json.loads(text) if text else default
        except Exception:
            self.errors += 1
            self.ok = False
            return default

    async def publish(self, name: str, data: Any) -> bool:
        if not self.ok or self.client is None:
            return False
        try:
            await self.client.publish(name, json.dumps(data, default=str, separators=(",", ":")))
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            self.ok = False
            return False

    def stats(self) -> dict[str, Any]:
        return {"kind": "redis", "ok": self.ok, "url": self.url, "reads": self.reads, "writes": self.writes, "errors": self.errors}


class FileStore:
    def __init__(self, folder: str = "./saved_data") -> None:
        self.folder = Path(folder)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.reads = 0
        self.writes = 0
        self.errors = 0

    def sim_path(self, sim_id: str) -> Path:
        return self.folder / f"sim_{sim_id}.json"

    def exp_path(self, experiment_id: str) -> Path:
        return self.folder / f"exp_{experiment_id}.json"

    async def save_sim(self, state: SimState) -> bool:
        try:
            await asyncio.to_thread(self.sim_path(state.id).write_text, json.dumps(state.to_dict(), separators=(",", ":")), "utf-8")
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            return False

    async def get_sim(self, sim_id: str) -> SimState | None:
        path = self.sim_path(sim_id)
        if not path.exists():
            return None
        try:
            text = await asyncio.to_thread(path.read_text, "utf-8")
            self.reads += 1
            return SimState.from_dict(json.loads(text))
        except Exception:
            self.errors += 1
            return None

    async def delete_sim(self, sim_id: str) -> bool:
        path = self.sim_path(sim_id)
        if not path.exists():
            return False
        try:
            await asyncio.to_thread(path.unlink)
            return True
        except Exception:
            self.errors += 1
            return False

    async def save_experiment(self, item: Experiment) -> bool:
        try:
            await asyncio.to_thread(self.exp_path(item.id).write_text, json.dumps(item.to_dict(), separators=(",", ":")), "utf-8")
            self.writes += 1
            return True
        except Exception:
            self.errors += 1
            return False

    async def get_experiment(self, experiment_id: str) -> Experiment | None:
        path = self.exp_path(experiment_id)
        if not path.exists():
            return None
        try:
            text = await asyncio.to_thread(path.read_text, "utf-8")
            self.reads += 1
            return Experiment.from_dict(json.loads(text))
        except Exception:
            self.errors += 1
            return None

    async def list_sim_ids(self) -> list[str]:
        vals = []
        for path in self.folder.glob("sim_*.json"):
            vals.append(path.stem[4:])
        return sorted(vals)

    async def list_experiment_ids(self) -> list[str]:
        vals = []
        for path in self.folder.glob("exp_*.json"):
            vals.append(path.stem[4:])
        return sorted(vals)

    def stats(self) -> dict[str, Any]:
        return {
            "kind": "file",
            "folder": str(self.folder),
            "sims": len(list(self.folder.glob("sim_*.json"))),
            "experiments": len(list(self.folder.glob("exp_*.json"))),
            "reads": self.reads,
            "writes": self.writes,
            "errors": self.errors,
        }


class MixedStore:
    def __init__(self) -> None:
        self.memory = MemoryStore()
        self.redis = RedisStore()
        self.files = FileStore()
        self.use_files = False

    async def start(self) -> dict[str, Any]:
        redis_ok = await self.redis.start()
        return {"redis": redis_ok, "memory": True, "files": self.use_files}

    async def stop(self) -> None:
        await self.redis.stop()

    async def save_sim(self, state: SimState) -> SimState:
        await self.memory.save_sim(state)
        await self.redis.save_sim(state)
        if self.use_files:
            await self.files.save_sim(state)
        return state

    async def get_sim(self, sim_id: str) -> SimState | None:
        item = await self.memory.get_sim(sim_id)
        if item is not None:
            return item
        item = await self.redis.get_sim(sim_id)
        if item is not None:
            await self.memory.save_sim(item)
            return item
        if self.use_files:
            item = await self.files.get_sim(sim_id)
            if item is not None:
                await self.memory.save_sim(item)
                return item
        return None

    async def delete_sim(self, sim_id: str) -> bool:
        a = await self.memory.delete_sim(sim_id)
        b = await self.redis.delete_sim(sim_id)
        c = await self.files.delete_sim(sim_id) if self.use_files else False
        return a or b or c

    async def save_experiment(self, item: Experiment) -> Experiment:
        await self.memory.save_experiment(item)
        await self.redis.save_experiment(item)
        if self.use_files:
            await self.files.save_experiment(item)
        return item

    async def get_experiment(self, experiment_id: str) -> Experiment | None:
        item = await self.memory.get_experiment(experiment_id)
        if item is not None:
            return item
        item = await self.redis.get_experiment(experiment_id)
        if item is not None:
            await self.memory.save_experiment(item)
            return item
        if self.use_files:
            item = await self.files.get_experiment(experiment_id)
            if item is not None:
                await self.memory.save_experiment(item)
                return item
        return None

    def stats(self) -> dict[str, Any]:
        return {"memory": self.memory.stats(), "redis": self.redis.stats(), "files": self.files.stats(), "use_files": self.use_files}


store = MixedStore()
