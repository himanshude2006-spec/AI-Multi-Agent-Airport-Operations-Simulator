from __future__ import annotations

import asyncio
from typing import Any, Literal

from fastapi import APIRouter, BackgroundTasks, HTTPException, Query, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from app.other.ai import Advice, advisor
from app.data.db import database
from app.airport.engine import SimEngine, engine_store, experiment_runner
from app.web.events import EventFilter, bus
from app.airport.metrics import event_report, fuel_report, delay_report, airline_report, gate_report, runway_report
from app.airport.schedule import algorithm_names, rank_flights
from app.other.settings import public_settings, settings
from app.data.store import store
from app.other.types import Algorithm, EventKind, SimConfig, WeatherKind
from app.airport.weather import WeatherMaker, weather_names, weather_rule


router = APIRouter()


class SimCreate(BaseModel):
    name: str = "Airport Test"
    seed: int = 42
    algorithm: Algorithm = Algorithm.WEIGHTED
    flight_count: int = Field(default=30, ge=1, le=500)
    runway_count: int = Field(default=3, ge=1, le=20)
    gate_count: int = Field(default=12, ge=1, le=100)
    max_ticks: int = Field(default=1000, ge=10, le=20000)
    tick_seconds: int = Field(default=60, ge=1, le=3600)
    start_weather: WeatherKind = WeatherKind.CLEAR
    weather_on: bool = True
    failures_on: bool = True
    ai_on: bool = False
    random_arrivals: bool = True
    arrival_window: int = Field(default=80, ge=0, le=5000)
    emergency_rate: float = Field(default=0.03, ge=0, le=1)
    failure_rate: float = Field(default=0.01, ge=0, le=1)
    weather_change_rate: float = Field(default=0.08, ge=0, le=1)
    low_fuel: float = Field(default=25.0, gt=0)
    critical_fuel: float = Field(default=12.0, gt=0)
    diversion_fuel: float = Field(default=6.0, ge=0)
    holding_fuel_cost: float = Field(default=0.7, ge=0)
    landing_fuel_cost: float = Field(default=2.0, ge=0)
    gate_hold_time: int = Field(default=18, ge=1)
    landing_time: int = Field(default=3, ge=1)
    runway_gap: int = Field(default=2, ge=0)
    passenger_weight: float = 0.02
    wait_weight: float = 1.1
    fuel_weight: float = 2.3
    emergency_weight: float = 100.0
    size_weight: float = 1.5
    fairness_weight: float = 1.0
    airport_code: str = "SIM"
    notes: dict[str, Any] = Field(default_factory=dict)

    def to_config(self) -> SimConfig:
        return SimConfig.from_dict(self.model_dump(mode="json"))


class TickBody(BaseModel):
    ticks: int = Field(default=1, ge=1, le=5000)


class RunBody(BaseModel):
    max_ticks: int | None = Field(default=None, ge=1, le=20000)
    background: bool = False


class FlightCreate(BaseModel):
    airline: str = "XX"
    number: str = "100"
    aircraft: str = "A320"
    category: str | None = None
    passengers: int | None = Field(default=None, ge=0)
    fuel: float = Field(default=60.0, ge=0)
    arrival_tick: int = Field(default=0, ge=0)
    runway_need: int | None = Field(default=None, ge=1)
    origin: str = "UNK"
    emergency: bool = False


class RunwayCreate(BaseModel):
    name: str | None = None
    length: int = Field(default=3000, ge=500, le=10000)


class GateCreate(BaseModel):
    name: str | None = None
    categories: list[str] = Field(default_factory=lambda: ["small", "medium", "large"])


class WeatherBody(BaseModel):
    kind: WeatherKind
    level: int | None = Field(default=None, ge=0, le=5)


class EmergencyBody(BaseModel):
    reason: str = "manual emergency"


class DivertBody(BaseModel):
    reason: str = "manual diversion"


class RunwayCloseBody(BaseModel):
    ticks: int = Field(default=5, ge=1, le=500)
    reason: str = "manual closure"


class AdviceBody(BaseModel):
    use_ai: bool = True


class AdviceApplyBody(BaseModel):
    advice_id: str | None = None
    action: str | None = None
    target: str = ""
    reason: str = ""
    confidence: float = Field(default=0.5, ge=0, le=1)
    source: str = "manual"
    data: dict[str, Any] = Field(default_factory=dict)


class ExperimentCreate(BaseModel):
    name: str = "Algorithm Comparison"
    algorithms: list[Algorithm] = Field(default_factory=lambda: [Algorithm.FCFS, Algorithm.FUEL, Algorithm.WEIGHTED, Algorithm.SOLVER])
    runs: int = Field(default=3, ge=1, le=50)
    config: SimCreate = Field(default_factory=SimCreate)
    background: bool = False


async def save_engine(engine: SimEngine) -> None:
    await store.save_sim(engine.state)
    if settings.use_database and database.ready:
        await asyncio.to_thread(database.save_sim, engine.state)
        if settings.save_events:
            await asyncio.to_thread(database.save_events, engine.state.events)
        if settings.save_snapshots and engine.snapshots:
            snap = engine.snapshots[-1]
            await asyncio.to_thread(database.save_snapshot, engine.state.id, engine.state.tick, snap)


async def run_and_save(engine: SimEngine, max_ticks: int | None = None) -> None:
    await engine.run(max_ticks)
    await save_engine(engine)


async def run_experiment_and_save(item) -> None:
    await experiment_runner.run(item)
    await store.save_experiment(item)
    if settings.use_database and database.ready:
        await asyncio.to_thread(database.save_experiment, item)


def need_engine(sim_id: str) -> SimEngine:
    item = engine_store.get(sim_id)
    if item is None:
        raise HTTPException(status_code=404, detail="simulation not found")
    return item


def state_output(engine: SimEngine, include_events: bool = False) -> dict[str, Any]:
    data = engine.state.to_dict(include_events=include_events)
    data["scheduler"] = engine.scheduler_info()
    data["checks"] = engine.check()
    return data


@router.get("/health")
async def health() -> dict[str, Any]:
    return {
        "ok": True,
        "name": settings.app_name,
        "version": settings.app_version,
        "database": database.stats(),
        "store": store.stats(),
        "events": bus.stats(),
        "engines": engine_store.stats(),
        "ai": advisor.stats(),
    }


@router.get("/settings")
async def get_settings() -> dict[str, Any]:
    return public_settings()


@router.get("/catalog")
async def catalog() -> dict[str, Any]:
    maker = WeatherMaker(1)
    return {
        "algorithms": algorithm_names(),
        "weather": weather_names(),
        "weather_rules": maker.catalog(),
        "event_kinds": [x.value for x in EventKind],
    }


@router.get("/weather/{name}")
async def weather_info(name: str) -> dict[str, Any]:
    try:
        return weather_rule(name)
    except Exception:
        raise HTTPException(status_code=404, detail="weather type not found")


@router.post("/simulations")
async def create_sim(body: SimCreate) -> dict[str, Any]:
    config = body.to_config()
    problems = config.check()
    if problems:
        raise HTTPException(status_code=422, detail=problems)
    engine = await engine_store.create(config)
    await save_engine(engine)
    return state_output(engine, include_events=False)


@router.get("/simulations")
async def list_sims(
    status: str = "",
    algorithm: str = "",
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
) -> dict[str, Any]:
    vals = []
    for engine in engine_store.list():
        if status and engine.state.status != status:
            continue
        if algorithm and engine.state.config.algorithm.value != algorithm:
            continue
        vals.append({
            "id": engine.state.id,
            "name": engine.state.config.name,
            "status": engine.state.status,
            "algorithm": engine.state.config.algorithm.value,
            "tick": engine.state.tick,
            "flights": len(engine.state.flights),
            "completed": engine.state.metrics.completed,
            "diverted": engine.state.metrics.diverted,
            "average_delay": engine.state.metrics.average_delay,
            "overall_score": engine.state.metrics.overall_score,
            "created_at": engine.state.created_at,
            "updated_at": engine.state.updated_at,
        })
    vals = vals[offset:offset + limit]
    return {"items": vals, "count": len(vals), "store": engine_store.stats()}


@router.get("/simulations/{sim_id}")
async def get_sim(sim_id: str, include_events: bool = False) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return state_output(engine, include_events=include_events)


@router.delete("/simulations/{sim_id}")
async def delete_sim(sim_id: str) -> dict[str, Any]:
    found = await engine_store.delete(sim_id)
    await store.delete_sim(sim_id)
    if settings.use_database and database.ready:
        await asyncio.to_thread(database.delete_sim, sim_id)
    if not found:
        raise HTTPException(status_code=404, detail="simulation not found")
    bus.clear(sim_id)
    return {"deleted": True, "sim_id": sim_id}


@router.post("/simulations/{sim_id}/start")
async def start_sim(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    await engine.start()
    await save_engine(engine)
    return state_output(engine)


@router.post("/simulations/{sim_id}/pause")
async def pause_sim(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    await engine.pause()
    await save_engine(engine)
    return state_output(engine)


@router.post("/simulations/{sim_id}/tick")
async def tick_sim(sim_id: str, body: TickBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    for _ in range(body.ticks):
        if engine.state.status == "completed":
            break
        await engine.one_tick()
    await save_engine(engine)
    return state_output(engine)


@router.post("/simulations/{sim_id}/run")
async def run_sim(sim_id: str, body: RunBody, background_tasks: BackgroundTasks) -> dict[str, Any]:
    engine = need_engine(sim_id)
    if body.background:
        background_tasks.add_task(run_and_save, engine, body.max_ticks)
        return {"started": True, "background": True, "sim_id": sim_id, "status": engine.state.status}
    await run_and_save(engine, body.max_ticks)
    return state_output(engine)


@router.post("/simulations/{sim_id}/run-until/{tick}")
async def run_until(sim_id: str, tick: int) -> dict[str, Any]:
    engine = need_engine(sim_id)
    await engine.run_until(tick)
    await save_engine(engine)
    return state_output(engine)


@router.get("/simulations/{sim_id}/metrics")
async def get_metrics(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return engine.report()


@router.get("/simulations/{sim_id}/metrics/summary")
async def get_metric_summary(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    state = engine.state
    return {
        "metrics": state.metrics.to_dict(),
        "fuel": fuel_report(state),
        "delay": delay_report(state),
        "events": event_report(state),
        "airlines": airline_report(state),
        "runways": runway_report(state),
        "gates": gate_report(state),
    }


@router.get("/simulations/{sim_id}/events")
async def get_events(
    sim_id: str,
    limit: int = Query(default=200, ge=1, le=5000),
    min_tick: int = Query(default=0, ge=0),
    kind: list[EventKind] | None = Query(default=None),
    flight_id: str = "",
    runway_id: str = "",
    gate_id: str = "",
    text: str = "",
) -> dict[str, Any]:
    engine = need_engine(sim_id)
    fil = EventFilter(kinds=set(kind or []), min_tick=min_tick, flight_id=flight_id, runway_id=runway_id, gate_id=gate_id, text=text)
    vals = [x for x in engine.state.events if fil.match(x)]
    vals = vals[-limit:]
    return {"items": [x.to_dict() for x in vals], "count": len(vals), "all_count": len(engine.state.events)}


@router.get("/simulations/{sim_id}/flights")
async def get_flights(sim_id: str, status: str = "", airline: str = "", risk: str = "") -> dict[str, Any]:
    engine = need_engine(sim_id)
    vals = []
    for flight in engine.state.flights:
        if status and flight.status.value != status:
            continue
        if airline and flight.airline != airline:
            continue
        if risk and flight.risk() != risk:
            continue
        vals.append(flight.to_dict())
    return {"items": vals, "count": len(vals)}


@router.get("/simulations/{sim_id}/flights/{flight_id}")
async def get_flight(sim_id: str, flight_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    flight = engine.state.flight(flight_id)
    if flight is None:
        raise HTTPException(status_code=404, detail="flight not found")
    vals = [x.to_dict() for x in engine.state.events if x.data.get("flight_id") == flight_id]
    return {"flight": flight.to_dict(), "events": vals}


@router.post("/simulations/{sim_id}/flights")
async def add_flight(sim_id: str, body: FlightCreate) -> dict[str, Any]:
    engine = need_engine(sim_id)
    data = body.model_dump(exclude_none=True)
    flight = await engine.add_flight(data)
    await save_engine(engine)
    return flight.to_dict()


@router.post("/simulations/{sim_id}/flights/{flight_id}/emergency")
async def mark_emergency(sim_id: str, flight_id: str, body: EmergencyBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    try:
        flight = await engine.mark_emergency(flight_id, body.reason)
    except KeyError:
        raise HTTPException(status_code=404, detail="flight not found")
    await save_engine(engine)
    return flight.to_dict()


@router.post("/simulations/{sim_id}/flights/{flight_id}/divert")
async def divert_flight(sim_id: str, flight_id: str, body: DivertBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    try:
        flight = await engine.divert_flight(flight_id, body.reason)
    except KeyError:
        raise HTTPException(status_code=404, detail="flight not found")
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    await save_engine(engine)
    return flight.to_dict()


@router.get("/simulations/{sim_id}/runways")
async def get_runways(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return {"items": [x.to_dict() for x in engine.state.runways], "count": len(engine.state.runways)}


@router.post("/simulations/{sim_id}/runways")
async def add_runway(sim_id: str, body: RunwayCreate) -> dict[str, Any]:
    engine = need_engine(sim_id)
    item = await engine.add_runway(body.model_dump(exclude_none=True))
    await save_engine(engine)
    return item.to_dict()


@router.post("/simulations/{sim_id}/runways/{runway_id}/close")
async def close_runway(sim_id: str, runway_id: str, body: RunwayCloseBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    try:
        item = await engine.close_runway(runway_id, body.ticks, body.reason)
    except KeyError:
        raise HTTPException(status_code=404, detail="runway not found")
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    await save_engine(engine)
    return item.to_dict()


@router.post("/simulations/{sim_id}/runways/{runway_id}/open")
async def open_runway(sim_id: str, runway_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    try:
        item = await engine.open_runway(runway_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="runway not found")
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    await save_engine(engine)
    return item.to_dict()


@router.get("/simulations/{sim_id}/gates")
async def get_gates(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return {"items": [x.to_dict() for x in engine.state.gates], "count": len(engine.state.gates)}


@router.post("/simulations/{sim_id}/gates")
async def add_gate(sim_id: str, body: GateCreate) -> dict[str, Any]:
    engine = need_engine(sim_id)
    item = await engine.add_gate(body.model_dump(exclude_none=True))
    await save_engine(engine)
    return item.to_dict()


@router.post("/simulations/{sim_id}/weather")
async def force_weather(sim_id: str, body: WeatherBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    item = await engine.force_weather(body.kind.value, body.level)
    await save_engine(engine)
    return item.to_dict()


@router.get("/simulations/{sim_id}/scheduler")
async def scheduler_info(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return engine.scheduler_info()


@router.get("/simulations/{sim_id}/scheduler/rank")
async def scheduler_rank(sim_id: str, algorithm: Algorithm | None = None) -> dict[str, Any]:
    engine = need_engine(sim_id)
    name = algorithm or engine.state.config.algorithm
    vals = rank_flights(engine.state, name)
    return {"algorithm": name.value, "items": vals, "count": len(vals)}


@router.get("/simulations/{sim_id}/scheduler/compare")
async def scheduler_compare(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return engine.compare_picks()


@router.post("/simulations/{sim_id}/ai")
async def ask_advice(sim_id: str, body: AdviceBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    vals = await advisor.recommend(engine, use_ai=body.use_ai)
    await save_engine(engine)
    return {"items": [x.to_dict() for x in vals], "count": len(vals), "ai": advisor.stats()}


@router.post("/simulations/{sim_id}/ai/apply")
async def apply_advice(sim_id: str, body: AdviceApplyBody) -> dict[str, Any]:
    engine = need_engine(sim_id)
    item = None
    if body.advice_id:
        item = advisor.get(engine, body.advice_id)
    if item is None:
        if not body.action:
            raise HTTPException(status_code=422, detail="action or advice_id is required")
        item = Advice.make(engine, body.action, body.target, body.reason, body.confidence, body.source, body.data)
    item = await advisor.apply(engine, item)
    engine.state.ai_items.append(item.to_dict())
    if settings.use_database and database.ready:
        await asyncio.to_thread(database.save_ai, engine.state.id, engine.state.tick, item.to_dict())
    await save_engine(engine)
    return item.to_dict()


@router.get("/simulations/{sim_id}/ai")
async def get_advice(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return {"items": engine.state.ai_items, "count": len(engine.state.ai_items)}


@router.get("/simulations/{sim_id}/check")
async def check_sim(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    vals = engine.check()
    return {"ok": not vals, "problems": vals}


@router.post("/simulations/{sim_id}/repair")
async def repair_sim(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    vals = engine.repair()
    await save_engine(engine)
    return {"fixed": vals, "count": len(vals), "problems": engine.check()}


@router.get("/simulations/{sim_id}/snapshots")
async def get_snapshots(sim_id: str) -> dict[str, Any]:
    engine = need_engine(sim_id)
    return {"items": engine.snapshots, "count": len(engine.snapshots)}


@router.post("/experiments")
async def create_experiment(body: ExperimentCreate, background_tasks: BackgroundTasks) -> dict[str, Any]:
    item = await experiment_runner.make(body.name, body.algorithms, body.runs, body.config.to_config())
    if body.background:
        background_tasks.add_task(run_experiment_and_save, item)
        return {"id": item.id, "status": item.status, "background": True}
    await run_experiment_and_save(item)
    return item.to_dict()


@router.get("/experiments")
async def list_experiments() -> dict[str, Any]:
    vals = [x.to_dict() for x in experiment_runner.list()]
    return {"items": vals, "count": len(vals)}


@router.get("/experiments/{experiment_id}")
async def get_experiment(experiment_id: str) -> dict[str, Any]:
    item = experiment_runner.get(experiment_id)
    if item is None:
        raise HTTPException(status_code=404, detail="experiment not found")
    return item.to_dict()


@router.delete("/experiments/{experiment_id}")
async def delete_experiment(experiment_id: str) -> dict[str, Any]:
    if not experiment_runner.delete(experiment_id):
        raise HTTPException(status_code=404, detail="experiment not found")
    return {"deleted": True, "experiment_id": experiment_id}


@router.websocket("/ws/{sim_id}")
async def simulation_socket(ws: WebSocket, sim_id: str) -> None:
    if engine_store.get(sim_id) is None:
        await ws.accept()
        await ws.send_json({"kind": "error", "detail": "simulation not found"})
        await ws.close(code=1008)
        return
    await bus.hub.connect(sim_id, ws)
    await bus.replay(sim_id, ws, limit=100)
    try:
        while True:
            data = await ws.receive_json()
            name = str(data.get("action", ""))
            if name == "filter":
                await bus.hub.set_filter(ws, data.get("filter", {}))
                await ws.send_json({"kind": "filter_set"})
            elif name == "replay":
                await bus.replay(sim_id, ws, limit=int(data.get("limit", 100)))
            elif name == "state":
                engine = need_engine(sim_id)
                await ws.send_json({"kind": "state", "data": engine.state.to_dict(include_events=False)})
            elif name == "ping":
                await ws.send_json({"kind": "pong", "sim_id": sim_id})
            else:
                await ws.send_json({"kind": "unknown_action", "action": name})
    except WebSocketDisconnect:
        await bus.hub.disconnect(sim_id, ws)
    except Exception:
        await bus.hub.disconnect(sim_id, ws)
