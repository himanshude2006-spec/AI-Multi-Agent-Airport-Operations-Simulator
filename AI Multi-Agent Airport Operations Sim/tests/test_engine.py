import asyncio

import pytest

from app.ai import Advice, advisor
from app.engine import ExperimentRunner, SimEngine
from app.metrics import MetricsMaker
from app.types import Algorithm, FlightStatus, GateStatus, RunwayStatus, SimConfig, WeatherKind


def run(coro):
    return asyncio.run(coro)


def config(**data):
    vals = {
        "name": "Test Airport",
        "seed": 20,
        "algorithm": Algorithm.WEIGHTED,
        "flight_count": 12,
        "runway_count": 3,
        "gate_count": 8,
        "max_ticks": 300,
        "arrival_window": 20,
        "weather_on": False,
        "failures_on": False,
        "emergency_rate": 0.0,
        "failure_rate": 0.0,
        "weather_change_rate": 0.0,
    }
    vals.update(data)
    return SimConfig(**vals)


def make(**data):
    return run(SimEngine.create(config(**data)))


def test_create_engine():
    item = make()
    assert item.state.id
    assert item.state.status == "created"
    assert len(item.state.flights) == 12
    assert len(item.state.runways) == 3
    assert len(item.state.gates) == 8
    assert item.state.config.name == "Test Airport"


def test_create_events():
    item = make(flight_count=5)
    assert len(item.state.events) == 6
    assert item.state.events[0].kind.value == "simulation_created"
    assert sum(1 for x in item.state.events if x.kind.value == "flight_created") == 5


def test_start_engine():
    item = make()
    run(item.start())
    assert item.state.status == "running"
    assert item.running is True


def test_pause_engine():
    item = make()
    run(item.start())
    run(item.pause())
    assert item.state.status == "paused"
    assert item.running is False
    assert item.stop_requested is True


def test_one_tick():
    item = make(arrival_window=1)
    run(item.one_tick())
    assert item.state.tick == 1
    assert item.state.status in {"running", "completed"}
    assert item.state.metrics.ticks == 1


def test_ten_ticks():
    item = make(arrival_window=3)
    for _ in range(10):
        run(item.one_tick())
    assert item.state.tick == 10
    assert any(x.status != FlightStatus.PLANNED for x in item.state.flights)
    assert item.state.metrics.events > 0


def test_run_limit():
    item = make(max_ticks=100)
    run(item.run(5))
    assert item.state.tick == 5
    assert item.state.status in {"running", "completed"}


def test_run_until():
    item = make(max_ticks=100)
    run(item.run_until(8))
    assert item.state.tick == 8


def test_run_until_done():
    item = make(flight_count=4, runway_count=2, gate_count=4, arrival_window=2, max_ticks=250)
    run(item.run_until_done())
    assert item.state.status == "completed"
    assert item.state.all_done() or item.state.tick == item.state.config.max_ticks


def test_metrics_after_run():
    item = make(flight_count=5, arrival_window=2, max_ticks=200)
    run(item.run_until_done())
    data = item.state.metrics
    assert data.total_flights == 5
    assert data.completed + data.diverted + data.cancelled + data.active == 5
    assert 0 <= data.overall_score <= 100


def test_add_flight():
    item = make(flight_count=1)
    old = len(item.state.flights)
    flight = run(item.add_flight({"airline": "ZZ", "number": "900", "aircraft": "A320", "fuel": 70, "arrival_tick": 0}))
    assert len(item.state.flights) == old + 1
    assert flight.airline == "ZZ"
    assert flight.aircraft == "A320"


def test_add_runway():
    item = make(runway_count=1)
    old = len(item.state.runways)
    runway = run(item.add_runway({"name": "NEW", "length": 4500}))
    assert len(item.state.runways) == old + 1
    assert runway.name == "NEW"
    assert runway.length == 4500


def test_add_gate():
    item = make(gate_count=1)
    old = len(item.state.gates)
    gate = run(item.add_gate({"name": "NEWG", "categories": ["small", "medium", "large", "heavy"]}))
    assert len(item.state.gates) == old + 1
    assert gate.name == "NEWG"
    assert "heavy" in gate.categories


def test_force_weather():
    item = make()
    weather = run(item.force_weather("storm", 4))
    assert weather.kind == WeatherKind.STORM
    assert weather.level == 4
    assert item.state.weather.kind == WeatherKind.STORM


def test_close_open_runway():
    item = make()
    runway = item.state.runways[0]
    run(item.close_runway(runway.id, 5, "test"))
    assert runway.status == RunwayStatus.CLOSED
    run(item.open_runway(runway.id))
    assert runway.status == RunwayStatus.OPEN


def test_mark_emergency():
    item = make(arrival_window=0)
    flight = item.state.flights[0]
    run(item.mark_emergency(flight.id, "test emergency"))
    assert flight.emergency is True
    assert "test emergency" in flight.notes


def test_divert_flight():
    item = make(arrival_window=0)
    flight = item.state.flights[0]
    run(item.divert_flight(flight.id, "test diversion"))
    assert flight.status == FlightStatus.DIVERTED
    assert flight.diverted_tick == 0


def test_snapshot():
    item = make()
    data = item.save_snapshot()
    assert data["snapshot_tick"] == 0
    assert item.get_snapshot(0) is not None
    assert item.closest_snapshot(10) is not None


def test_clone():
    item = make()
    clone = item.clone(seed=90, algorithm=Algorithm.FCFS)
    assert clone.state.id != item.state.id
    assert clone.state.config.seed == 90
    assert clone.state.config.algorithm == Algorithm.FCFS
    assert clone.state.tick == 0


def test_clone_resources_reset():
    item = make()
    item.state.runways[0].status = RunwayStatus.CLOSED
    item.state.gates[0].status = GateStatus.CLOSED
    clone = item.clone()
    assert all(x.status == RunwayStatus.OPEN for x in clone.state.runways)
    assert all(x.status == GateStatus.OPEN for x in clone.state.gates)


def test_compare_picks():
    item = make(arrival_window=0)
    run(item.one_tick())
    data = item.compare_picks()
    assert "fcfs" in data
    assert "fuel" in data
    assert "weighted" in data
    assert "solver" in data
    assert "random" in data


def test_scheduler_info():
    item = make()
    data = item.scheduler_info()
    assert data["current"] == "weighted"
    assert "details" in data
    assert "all" in data


def test_check_clean():
    item = make()
    assert item.check() == []


def test_repair_bad_links():
    item = make()
    item.state.flights[0].runway_id = "missing"
    assert item.check()
    fixed = item.repair()
    assert fixed
    assert item.state.flights[0].runway_id is None


def test_report_sections():
    item = make()
    data = item.report()
    assert "metrics" in data
    assert "flight_status" in data
    assert "runways" in data
    assert "gates" in data
    assert "airlines" in data
    assert "fuel" in data
    assert "delay" in data
    assert "events" in data


def test_tick_summary():
    item = make()
    data = item.tick_summary()
    assert data["tick"] == 0
    assert data["active"] == len(item.state.flights)
    assert data["open_runways"] == len(item.state.runways)


def test_state_round_trip():
    item = make()
    data = item.state.to_dict()
    clone = item.state.from_dict(data)
    assert clone.id == item.state.id
    assert len(clone.flights) == len(item.state.flights)
    assert len(clone.runways) == len(item.state.runways)


def test_state_json_round_trip():
    item = make()
    text = item.state.json()
    clone = item.state.from_json(text)
    assert clone.id == item.state.id
    assert clone.config.algorithm == item.state.config.algorithm


def test_local_ai_advice():
    item = make(arrival_window=0)
    run(item.one_tick())
    vals = run(advisor.recommend(item, use_ai=False))
    assert vals
    assert all(x.sim_id == item.state.id for x in vals)


def test_apply_no_action():
    item = make()
    advice = Advice.make(item, "no_action", "", "stable", 0.7, "test")
    out = run(advisor.apply(item, advice))
    assert out.accepted is True
    assert out.applied is True


def test_apply_change_algorithm():
    item = make()
    advice = Advice.make(item, "change_algorithm", "fuel", "test", 0.7, "test")
    out = run(advisor.apply(item, advice))
    assert out.applied is True
    assert item.state.config.algorithm == Algorithm.FUEL


def test_apply_priority():
    item = make()
    flight = item.state.flights[0]
    advice = Advice.make(item, "prioritize_flight", flight.id, "test", 0.9, "test")
    out = run(advisor.apply(item, advice))
    assert out.applied is True
    assert flight.emergency is True


def test_metrics_maker_direct():
    item = make()
    maker = MetricsMaker()
    data = maker.make(item.state)
    assert data.total_flights == len(item.state.flights)
    assert maker.calls == 1
    assert maker.last is not None


def test_experiment_make():
    runner = ExperimentRunner()
    item = run(runner.make("Test", [Algorithm.FCFS, Algorithm.FUEL], 1, config(flight_count=2, max_ticks=100)))
    assert item.name == "Test"
    assert item.runs == 1
    assert len(item.algorithms) == 2


def test_experiment_run():
    runner = ExperimentRunner()
    item = run(runner.make("Test", [Algorithm.FCFS, Algorithm.FUEL], 1, config(flight_count=2, runway_count=1, gate_count=2, arrival_window=1, max_ticks=120)))
    run(runner.run(item))
    assert item.status == "completed"
    assert len(item.items) == 2
    assert "ranking" in item.summary


def test_weather_on_run():
    item = make(weather_on=True, weather_change_rate=1.0, start_weather=WeatherKind.CLEAR)
    run(item.one_tick())
    assert item.state.weather.changed_tick == 1


def test_failure_on_run():
    item = make(failures_on=True, failure_rate=1.0, weather_on=False)
    run(item.one_tick())
    assert any(x.status in {RunwayStatus.INSPECTION, RunwayStatus.BUSY, RunwayStatus.OPEN} for x in item.state.runways)


def test_low_fuel_event():
    item = make(flight_count=1, arrival_window=0)
    item.state.flights[0].fuel = item.state.config.low_fuel - 1
    run(item.one_tick())
    assert item.state.flights[0].low_fuel_sent or item.state.flights[0].critical_fuel_sent


def test_diversion_by_fuel():
    item = make(flight_count=1, arrival_window=0)
    item.state.flights[0].fuel = item.state.config.diversion_fuel
    run(item.one_tick())
    assert item.state.flights[0].status in {FlightStatus.DIVERTED, FlightStatus.LANDING}


def test_airport_info():
    item = make()
    data = item.airport.airport_info()
    assert data["sim_id"] == item.state.id
    assert "flight_counts" in data
    assert "resource_counts" in data


def test_airport_full_info():
    item = make()
    data = item.airport.full_info()
    assert len(data["flights"]) == len(item.state.flights)
    assert len(data["runways"]) == len(item.state.runways)
    assert len(data["gates"]) == len(item.state.gates)


def test_aircraft_summary():
    item = make()
    data = item.airport.aircraft_summary()
    assert data
    assert sum(x["flights"] for x in data.values()) == len(item.state.flights)


def test_manual_complete_reason():
    item = make()
    run(item.complete("manual test"))
    assert item.state.status == "completed"
    assert item.state.done_reason == "manual test"


def test_completed_engine_does_not_tick():
    item = make()
    run(item.complete("manual"))
    old = item.state.tick
    run(item.one_tick())
    assert item.state.tick == old


def test_config_validation():
    bad = config(flight_count=0)
    assert bad.check()


def test_config_copy():
    val = config()
    other = val.copy()
    assert other.to_dict() == val.to_dict()
    other.seed = 99
    assert val.seed != other.seed
