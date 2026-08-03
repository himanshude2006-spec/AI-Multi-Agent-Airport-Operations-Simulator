from __future__ import annotations

import asyncio
from typing import Any

from app.other.ai import advisor
from app.data.db import database
from app.airport.engine import SimEngine, engine_store, experiment_runner
from app.other.settings import settings
from app.data.store import store
from app.other.types import Algorithm, Experiment, SimConfig, SimState

try:
    from celery import Celery
except Exception:
    Celery = None


class FakeTask:
    def __init__(self, fn):
        self.fn = fn
        self.name = fn.__name__

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

    def delay(self, *args, **kwargs):
        return {"task": self.name, "status": "celery_not_installed", "result": self.fn(*args, **kwargs)}

    def apply_async(self, args=None, kwargs=None, **opts):
        return self.delay(*(args or []), **(kwargs or {}))


class FakeCelery:
    def task(self, *args, **kwargs):
        def wrap(fn):
            return FakeTask(fn)
        if args and callable(args[0]):
            return FakeTask(args[0])
        return wrap

    def worker_main(self, *args, **kwargs):
        return 0


if Celery is not None:
    celery_app = Celery("airport_tasks", broker=settings.celery_broker_url, backend=settings.celery_result_url)
    celery_app.conf.update(
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        timezone=settings.timezone,
        enable_utc=True,
        task_track_started=True,
        worker_prefetch_multiplier=1,
        task_acks_late=True,
        result_expires=3600,
        broker_connection_retry_on_startup=True,
    )
else:
    celery_app = FakeCelery()


def run_async(fn):
    try:
        return asyncio.run(fn)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(fn)
        finally:
            loop.close()


def save_state(state: SimState) -> None:
    run_async(store.save_sim(state))
    if settings.use_database and database.ready:
        database.save_sim(state)
        if settings.save_events:
            database.save_events(state.events)


@celery_app.task(name="airport.create_simulation")
def create_simulation_task(config_data: dict[str, Any]) -> dict[str, Any]:
    config = SimConfig.from_dict(config_data)
    engine = run_async(SimEngine.create(config))
    run_async(engine_store.add(engine))
    save_state(engine.state)
    return {"sim_id": engine.state.id, "status": engine.state.status, "tick": engine.state.tick}


@celery_app.task(name="airport.run_simulation")
def run_simulation_task(state_data: dict[str, Any], max_ticks: int | None = None) -> dict[str, Any]:
    state = SimState.from_dict(state_data)
    engine = SimEngine.from_state(state)
    run_async(engine.run(max_ticks))
    save_state(engine.state)
    return engine.state.to_dict(include_events=False)


@celery_app.task(name="airport.run_saved_simulation")
def run_saved_simulation_task(sim_id: str, max_ticks: int | None = None) -> dict[str, Any]:
    state = run_async(store.get_sim(sim_id))
    if state is None and settings.use_database and database.ready:
        state = database.get_sim(sim_id)
    if state is None:
        return {"error": "simulation not found", "sim_id": sim_id}
    engine = SimEngine.from_state(state)
    run_async(engine.run(max_ticks))
    save_state(engine.state)
    return engine.state.to_dict(include_events=False)


@celery_app.task(name="airport.tick_simulation")
def tick_simulation_task(state_data: dict[str, Any], ticks: int = 1) -> dict[str, Any]:
    state = SimState.from_dict(state_data)
    engine = SimEngine.from_state(state)
    for _ in range(max(1, ticks)):
        if engine.state.status == "completed":
            break
        run_async(engine.one_tick())
    save_state(engine.state)
    return engine.state.to_dict(include_events=False)


@celery_app.task(name="airport.run_experiment")
def run_experiment_task(data: dict[str, Any]) -> dict[str, Any]:
    item = Experiment.from_dict(data)
    run_async(experiment_runner.run(item))
    run_async(store.save_experiment(item))
    if settings.use_database and database.ready:
        database.save_experiment(item)
    return item.to_dict()


@celery_app.task(name="airport.make_experiment")
def make_experiment_task(name: str, algorithms: list[str], runs: int, config_data: dict[str, Any]) -> dict[str, Any]:
    config = SimConfig.from_dict(config_data)
    vals = [Algorithm(x) for x in algorithms]
    item = run_async(experiment_runner.make(name, vals, runs, config))
    run_async(experiment_runner.run(item))
    run_async(store.save_experiment(item))
    if settings.use_database and database.ready:
        database.save_experiment(item)
    return item.to_dict()


@celery_app.task(name="airport.get_ai_advice")
def get_ai_advice_task(state_data: dict[str, Any], use_ai: bool = True) -> dict[str, Any]:
    state = SimState.from_dict(state_data)
    engine = SimEngine.from_state(state)
    vals = run_async(advisor.recommend(engine, use_ai=use_ai))
    save_state(engine.state)
    return {"items": [x.to_dict() for x in vals], "state": engine.state.to_dict(include_events=False)}


@celery_app.task(name="airport.save_simulation")
def save_simulation_task(state_data: dict[str, Any]) -> dict[str, Any]:
    state = SimState.from_dict(state_data)
    save_state(state)
    return {"saved": True, "sim_id": state.id, "tick": state.tick}


@celery_app.task(name="airport.cleanup_simulations")
def cleanup_simulations_task(keep: int = 100) -> dict[str, Any]:
    vals = engine_store.list()
    removed = []
    if len(vals) > keep:
        for engine in vals[keep:]:
            run_async(engine_store.delete(engine.state.id))
            removed.append(engine.state.id)
    return {"removed": removed, "count": len(removed), "remaining": engine_store.stats()}


@celery_app.task(name="airport.database_stats")
def database_stats_task() -> dict[str, Any]:
    if not database.ready:
        database.start()
    return database.stats()


@celery_app.task(name="airport.store_stats")
def store_stats_task() -> dict[str, Any]:
    return store.stats()


@celery_app.task(name="airport.health")
def health_task() -> dict[str, Any]:
    return {
        "ok": True,
        "name": settings.app_name,
        "database": database.stats(),
        "store": store.stats(),
        "engines": engine_store.stats(),
        "ai": advisor.stats(),
    }
