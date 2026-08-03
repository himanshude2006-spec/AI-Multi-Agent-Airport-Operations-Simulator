from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from typing import Any
from uuid import uuid4

from app.engine import SimEngine
from app.settings import settings
from app.types import EventKind, FlightStatus, RunwayStatus, WeatherKind

try:
    from openai import AsyncOpenAI
except Exception:
    AsyncOpenAI = None


@dataclass
class Advice:
    id: str
    sim_id: str
    tick: int
    action: str
    target: str
    reason: str
    confidence: float
    source: str
    accepted: bool = False
    applied: bool = False
    data: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        out = asdict(self)
        out["data"] = self.data or {}
        return out

    @classmethod
    def make(cls, engine: SimEngine, action: str, target: str, reason: str, confidence: float, source: str, data: dict[str, Any] | None = None) -> Advice:
        return cls(id=str(uuid4()), sim_id=engine.state.id, tick=engine.state.tick, action=action, target=target, reason=reason, confidence=confidence, source=source, data=data or {})


class AdviceValidator:
    def actions(self) -> set[str]:
        return {"prioritize_flight", "hold_flight", "divert_flight", "close_runway", "open_runway", "change_algorithm", "no_action"}

    def check(self, engine: SimEngine, item: Advice) -> list[str]:
        out = []
        if item.sim_id != engine.state.id:
            out.append("simulation id mismatch")
        if item.action not in self.actions():
            out.append("unknown action")
        if item.confidence < 0 or item.confidence > 1:
            out.append("confidence must be between 0 and 1")
        if item.action in {"prioritize_flight", "hold_flight", "divert_flight"}:
            flight = engine.state.flight(item.target)
            if flight is None:
                out.append("flight not found")
            elif flight.is_done():
                out.append("flight already finished")
        if item.action in {"close_runway", "open_runway"}:
            runway = engine.state.runway(item.target)
            if runway is None:
                out.append("runway not found")
        if item.action == "close_runway":
            runway = engine.state.runway(item.target)
            if runway is not None and runway.status == RunwayStatus.BUSY:
                out.append("busy runway cannot be closed")
        if item.action == "open_runway":
            runway = engine.state.runway(item.target)
            if runway is not None and runway.status == RunwayStatus.BUSY:
                out.append("busy runway cannot be opened")
        if item.action == "change_algorithm" and item.target not in {"fcfs", "fuel", "weighted", "solver", "random"}:
            out.append("unknown algorithm")
        return out

    def valid(self, engine: SimEngine, item: Advice) -> bool:
        return not self.check(engine, item)


class LocalAdvisor:
    def __init__(self) -> None:
        self.calls = 0

    def make(self, engine: SimEngine) -> list[Advice]:
        self.calls += 1
        out: list[Advice] = []
        state = engine.state
        waiting = [x for x in state.flights if x.is_waiting()]
        waiting.sort(key=lambda x: (not x.emergency, x.fuel, -x.wait_ticks))
        critical = [x for x in waiting if x.fuel <= state.config.critical_fuel]
        low = [x for x in waiting if x.fuel <= state.config.low_fuel]
        emergency = [x for x in waiting if x.emergency]
        open_runways = [x for x in state.runways if x.is_open()]
        closed_runways = [x for x in state.runways if x.status in {RunwayStatus.CLOSED, RunwayStatus.INSPECTION}]
        if emergency:
            flight = emergency[0]
            out.append(Advice.make(engine, "prioritize_flight", flight.id, f"{flight.label()} has an active emergency", 0.99, "local", {"fuel": flight.fuel, "wait": flight.wait_ticks}))
        elif critical:
            flight = critical[0]
            out.append(Advice.make(engine, "prioritize_flight", flight.id, f"{flight.label()} has critical fuel", 0.96, "local", {"fuel": flight.fuel, "wait": flight.wait_ticks}))
        elif low and open_runways:
            flight = low[0]
            out.append(Advice.make(engine, "prioritize_flight", flight.id, f"{flight.label()} has low fuel", 0.85, "local", {"fuel": flight.fuel, "wait": flight.wait_ticks}))
        if waiting and not open_runways:
            flight = waiting[0]
            if flight.fuel <= state.config.diversion_fuel + 2:
                out.append(Advice.make(engine, "divert_flight", flight.id, "no runway is open and fuel is near diversion level", 0.90, "local", {"fuel": flight.fuel}))
            else:
                out.append(Advice.make(engine, "hold_flight", flight.id, "no runway is currently open", 0.75, "local"))
        if state.weather.kind in {WeatherKind.STORM, WeatherKind.SNOW, WeatherKind.WIND} and state.weather.level >= 4:
            vals = [x for x in open_runways if x.flight_id is None]
            if vals:
                runway = min(vals, key=lambda x: x.length)
                out.append(Advice.make(engine, "close_runway", runway.id, f"severe {state.weather.kind.value} conditions", 0.78, "local", {"weather": state.weather.to_dict(), "ticks": 5}))
        if state.weather.kind == WeatherKind.CLEAR:
            for runway in closed_runways:
                if runway.failed_until <= state.tick:
                    out.append(Advice.make(engine, "open_runway", runway.id, "weather is clear and closure time has ended", 0.82, "local"))
                    break
        if len(waiting) >= max(8, len(state.runways) * 4) and state.config.algorithm == "fcfs":
            out.append(Advice.make(engine, "change_algorithm", "weighted", "large queue would benefit from weighted priority", 0.70, "local", {"waiting": len(waiting)}))
        if not out:
            out.append(Advice.make(engine, "no_action", "", "operations are stable", 0.65, "local"))
        return out


class AiAdvisor:
    def __init__(self) -> None:
        self.validator = AdviceValidator()
        self.local = LocalAdvisor()
        self.client = None
        self.calls = 0
        self.errors = 0
        if AsyncOpenAI is not None and settings.openai_api_key:
            self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    def state_data(self, engine: SimEngine) -> dict[str, Any]:
        state = engine.state
        waiting = []
        for flight in state.flights:
            if flight.is_waiting():
                waiting.append({
                    "id": flight.id,
                    "label": flight.label(),
                    "airline": flight.airline,
                    "aircraft": flight.aircraft,
                    "category": flight.category,
                    "passengers": flight.passengers,
                    "fuel": flight.fuel,
                    "wait_ticks": flight.wait_ticks,
                    "emergency": flight.emergency,
                    "runway_need": flight.runway_need,
                })
        runways = [{"id": x.id, "name": x.name, "length": x.length, "status": x.status.value, "busy_left": x.busy_left, "failed_until": x.failed_until} for x in state.runways]
        gates = [{"id": x.id, "name": x.name, "categories": x.categories, "status": x.status.value, "busy_left": x.busy_left} for x in state.gates]
        return {
            "simulation_id": state.id,
            "tick": state.tick,
            "algorithm": state.config.algorithm.value,
            "weather": state.weather.to_dict(),
            "waiting_flights": waiting,
            "runways": runways,
            "gates": gates,
            "metrics": state.metrics.to_dict(),
        }

    def system_text(self) -> str:
        return (
            "You advise an airport operations simulation. Return only JSON. "
            "Do not control the simulation directly. Suggest zero to three safe actions. "
            "Allowed actions are prioritize_flight, hold_flight, divert_flight, close_runway, open_runway, change_algorithm, no_action. "
            "Each item must contain action, target, reason, confidence, and data. "
            "Use exact ids from the supplied state. Avoid closing a busy runway."
        )

    def user_text(self, engine: SimEngine) -> str:
        return json.dumps(self.state_data(engine), separators=(",", ":"))

    async def ask_openai(self, engine: SimEngine) -> list[Advice]:
        if self.client is None:
            return []
        self.calls += 1
        try:
            res = await self.client.responses.create(
                model=settings.openai_model,
                input=[
                    {"role": "system", "content": self.system_text()},
                    {"role": "user", "content": self.user_text(engine)},
                ],
                temperature=settings.ai_temperature,
                max_output_tokens=settings.ai_max_tokens,
            )
            text = res.output_text
            data = json.loads(text)
            vals = data if isinstance(data, list) else data.get("items", [])
            out = []
            for row in vals[:3]:
                item = Advice.make(
                    engine,
                    str(row.get("action", "no_action")),
                    str(row.get("target", "")),
                    str(row.get("reason", "")),
                    float(row.get("confidence", 0.5)),
                    "openai",
                    dict(row.get("data", {})),
                )
                out.append(item)
            return out
        except Exception:
            self.errors += 1
            return []

    async def recommend(self, engine: SimEngine, use_ai: bool = True) -> list[Advice]:
        await engine.emit(EventKind.AI_REQUESTED, "AI recommendation requested", {"use_ai": use_ai})
        vals = await self.ask_openai(engine) if use_ai and settings.use_ai else []
        if not vals:
            vals = self.local.make(engine)
        out = []
        for item in vals:
            problems = self.validator.check(engine, item)
            item.accepted = not problems
            if problems:
                item.data = {**(item.data or {}), "validation_errors": problems}
                await engine.emit(EventKind.AI_REJECTED, "AI recommendation rejected", item.to_dict())
            else:
                await engine.emit(EventKind.AI_RECOMMENDED, "AI recommendation created", item.to_dict())
                out.append(item)
            engine.state.ai_items.append(item.to_dict())
        return out

    async def apply(self, engine: SimEngine, item: Advice) -> Advice:
        problems = self.validator.check(engine, item)
        if problems:
            item.accepted = False
            item.data = {**(item.data or {}), "validation_errors": problems}
            await engine.emit(EventKind.AI_REJECTED, "AI recommendation failed validation", item.to_dict())
            return item
        item.accepted = True
        if item.action == "prioritize_flight":
            flight = engine.flight(item.target)
            flight.emergency = True
            flight.add_note("AI priority")
            item.applied = True
        elif item.action == "hold_flight":
            flight = engine.flight(item.target)
            flight.add_note("AI hold")
            item.applied = True
        elif item.action == "divert_flight":
            await engine.divert_flight(item.target, item.reason or "AI diversion")
            item.applied = True
        elif item.action == "close_runway":
            ticks = int((item.data or {}).get("ticks", 5))
            await engine.close_runway(item.target, ticks, item.reason or "AI closure")
            item.applied = True
        elif item.action == "open_runway":
            await engine.open_runway(item.target)
            item.applied = True
        elif item.action == "change_algorithm":
            engine.state.config.algorithm = engine.state.config.algorithm.__class__(item.target)
            item.applied = True
        elif item.action == "no_action":
            item.applied = True
        if item.applied:
            await engine.emit(EventKind.AI_APPLIED, "AI recommendation applied", item.to_dict())
        return item

    def get(self, engine: SimEngine, advice_id: str) -> Advice | None:
        for row in engine.state.ai_items:
            if row.get("id") == advice_id:
                return Advice(**row)
        return None

    def stats(self) -> dict[str, Any]:
        return {"openai_ready": self.client is not None, "calls": self.calls, "errors": self.errors, "local_calls": self.local.calls, "model": settings.openai_model}


advisor = AiAdvisor()
