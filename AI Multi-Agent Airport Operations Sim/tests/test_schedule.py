import random

import pytest

from app.schedule import FCFSScheduler, FuelScheduler, RandomScheduler, SchedulerGroup, SolverScheduler, WeightedScheduler, airline_fairness, algorithm_names, compatible_count, jain_score, make_scheduler, rank_flights, wait_fairness
from app.types import Algorithm, Flight, FlightStatus, Gate, Runway, SimConfig, SimState


def flight(name, arrival, fuel, wait, passengers=100, need=2000, emergency=False, airline="AA"):
    item = Flight(
        id=name,
        airline=airline,
        number=name,
        aircraft="A320",
        category="medium",
        passengers=passengers,
        fuel=fuel,
        arrival_tick=arrival,
        runway_need=need,
        status=FlightStatus.HOLDING,
        wait_ticks=wait,
        emergency=emergency,
    )
    return item


def state(algorithm=Algorithm.WEIGHTED):
    cfg = SimConfig(algorithm=algorithm, seed=4, flight_count=4, runway_count=2, gate_count=2)
    item = SimState.make(cfg)
    item.tick = 20
    item.flights = [
        flight("F1", 1, 50, 5, 100, 2000, False, "AA"),
        flight("F2", 2, 10, 3, 80, 2200, False, "DL"),
        flight("F3", 3, 30, 10, 200, 2500, False, "UA"),
        flight("F4", 4, 40, 2, 150, 2100, True, "AA"),
    ]
    item.runways = [
        Runway(id="R1", name="R1", length=2400),
        Runway(id="R2", name="R2", length=3200),
    ]
    item.gates = [Gate(id="G1", name="G1", categories=["medium"]), Gate(id="G2", name="G2", categories=["medium", "large"])]
    return item


def test_algorithm_names():
    vals = algorithm_names()
    assert vals == ["fcfs", "fuel", "weighted", "solver", "random"]


def test_make_fcfs():
    assert isinstance(make_scheduler("fcfs"), FCFSScheduler)


def test_make_fuel():
    assert isinstance(make_scheduler("fuel"), FuelScheduler)


def test_make_weighted():
    assert isinstance(make_scheduler("weighted"), WeightedScheduler)


def test_make_solver():
    assert isinstance(make_scheduler("solver"), SolverScheduler)


def test_make_random():
    assert isinstance(make_scheduler("random"), RandomScheduler)


def test_fcfs_first():
    item = state(Algorithm.FCFS)
    vals = FCFSScheduler(4).select(item)
    assert vals
    assert vals[0].flight_id == "F1"


def test_fcfs_uses_two_runways():
    item = state(Algorithm.FCFS)
    vals = FCFSScheduler(4).select(item)
    assert len(vals) == 2
    assert len({x.runway_id for x in vals}) == 2


def test_fcfs_order():
    item = state(Algorithm.FCFS)
    vals = FCFSScheduler(4).order(item)
    assert vals[0]["flight_id"] == "F1"
    assert vals[-1]["flight_id"] == "F4"


def test_fuel_first():
    item = state(Algorithm.FUEL)
    vals = FuelScheduler(4).select(item)
    assert vals
    assert vals[0].flight_id in {"F2", "F4"}


def test_fuel_score_critical():
    item = state(Algorithm.FUEL)
    sch = FuelScheduler(4)
    low = sch.fuel_score(item.flights[1], item.config)
    normal = sch.fuel_score(item.flights[0], item.config)
    assert low > normal


def test_fuel_emergency_score():
    item = state(Algorithm.FUEL)
    sch = FuelScheduler(4)
    emergency = sch.fuel_score(item.flights[3], item.config)
    normal = sch.fuel_score(item.flights[0], item.config)
    assert emergency > normal


def test_weighted_emergency_first():
    item = state(Algorithm.WEIGHTED)
    vals = WeightedScheduler(4).select(item)
    assert vals
    assert vals[0].flight_id == "F4"


def test_weighted_score_parts():
    item = state()
    sch = WeightedScheduler(4)
    parts = sch.parts(item.flights[0], item.runways[0], item)
    assert parts.total > 0
    assert parts.passengers > 0
    assert parts.fit >= 0


def test_weighted_fit_bad():
    item = state()
    sch = WeightedScheduler(4)
    assert sch.fit_value(item.flights[2], item.runways[0]) < 0


def test_weighted_table():
    item = state()
    vals = WeightedScheduler(4).score_table(item)
    assert vals
    assert vals[0]["score"] >= vals[-1]["score"]


def test_weighted_order():
    item = state()
    vals = WeightedScheduler(4).order(item)
    assert vals[0]["rank"] == 1
    assert vals[-1]["rank"] == len(vals)


def test_random_repeatable():
    item = state(Algorithm.RANDOM)
    a = RandomScheduler(7).select(item.copy())
    b = RandomScheduler(7).select(item.copy())
    assert [x.to_dict() for x in a] == [x.to_dict() for x in b]


def test_random_different_seed():
    item = state(Algorithm.RANDOM)
    a = RandomScheduler(7).select(item.copy())
    b = RandomScheduler(8).select(item.copy())
    assert [x.score for x in a] != [x.score for x in b]


def test_solver_returns_picks():
    item = state(Algorithm.SOLVER)
    vals = SolverScheduler(4).select(item)
    assert vals
    assert all(x.reason for x in vals)


def test_solver_stats():
    item = state(Algorithm.SOLVER)
    sch = SolverScheduler(4)
    sch.select(item)
    data = sch.stats()
    assert "solve_status" in data
    assert "used_solver" in data


def test_group_get():
    group = SchedulerGroup(4)
    assert group.get("fcfs").name == "fcfs"
    assert group.get(Algorithm.WEIGHTED).name == "weighted"


def test_group_select():
    item = state(Algorithm.FUEL)
    group = SchedulerGroup(4)
    vals = group.select(item)
    assert vals
    assert group.get("fuel").calls == 1


def test_group_stats():
    group = SchedulerGroup(4)
    data = group.stats()
    assert set(data) == {"fcfs", "fuel", "weighted", "solver", "random"}


def test_group_compare():
    item = state()
    group = SchedulerGroup(4)
    data = group.compare_current(item)
    assert set(data) == {"fcfs", "fuel", "weighted", "solver", "random"}


def test_group_reset():
    item = state()
    group = SchedulerGroup(4)
    group.select(item)
    group.reset(9)
    assert all(x.calls == 0 for x in group.items.values())
    assert all(x.seed == 9 for x in group.items.values())


def test_compatible_count():
    item = state()
    assert compatible_count(item.flights, item.runways) == 7


def test_jain_equal():
    assert jain_score([1, 1, 1]) == 1.0


def test_jain_empty():
    assert jain_score([]) == 1.0


def test_jain_unequal():
    assert jain_score([1, 2, 10]) < 1.0


def test_wait_fairness_range():
    val = wait_fairness(state())
    assert 0 <= val <= 1


def test_airline_fairness_range():
    val = airline_fairness(state())
    assert 0 <= val <= 1


def test_rank_fcfs():
    vals = rank_flights(state(), "fcfs")
    assert vals[0]["flight_id"] == "F1"


def test_rank_fuel():
    vals = rank_flights(state(), "fuel")
    assert vals[0]["score"] >= vals[-1]["score"]


def test_rank_weighted():
    vals = rank_flights(state(), "weighted")
    assert vals[0]["rank"] == 1


def test_no_open_runways():
    item = state()
    for runway in item.runways:
        runway.close(item.tick)
    assert FCFSScheduler(4).select(item) == []
    assert FuelScheduler(4).select(item) == []
    assert WeightedScheduler(4).select(item) == []


def test_no_waiting_flights():
    item = state()
    for val in item.flights:
        val.status = FlightStatus.COMPLETED
    assert FCFSScheduler(4).select(item) == []


def test_runway_best_fit():
    item = state()
    sch = FCFSScheduler(4)
    runway = sch.best_runway(item.flights[0], item.runways)
    assert runway.id == "R1"


def test_runway_large_fit():
    item = state()
    sch = FCFSScheduler(4)
    runway = sch.best_runway(item.flights[2], item.runways)
    assert runway.id == "R2"


def test_scheduler_record():
    item = state()
    sch = FCFSScheduler(4)
    sch.select(item)
    assert sch.picks == 2
    assert sum(sch.airline_picks.values()) == 2


def test_scheduler_explain():
    item = state()
    sch = WeightedScheduler(4)
    data = sch.explain(item)
    assert data["algorithm"] == "weighted"
    assert data["waiting"] == 4
    assert data["open_runways"] == 2


def test_score_part_dict():
    item = state()
    sch = WeightedScheduler(4)
    data = sch.parts(item.flights[0], item.runways[0], item).to_dict()
    assert "total" in data
    assert isinstance(data["total"], float)


def test_pick_dict():
    item = state()
    pick = FCFSScheduler(4).select(item)[0]
    data = pick.to_dict()
    assert data["flight_id"]
    assert data["runway_id"]
    assert data["reason"]


def test_airline_delay_map():
    item = state()
    item.flights[0].delay_ticks = 10
    item.flights[3].delay_ticks = 20
    data = WeightedScheduler(4).airline_delay(item)
    assert data["AA"] == 15


def test_size_values():
    sch = WeightedScheduler(4)
    item = state().flights[0]
    item.category = "small"
    assert sch.size_value(item) == 1
    item.category = "super"
    assert sch.size_value(item) == 5


def test_fuel_order_rank():
    item = state()
    vals = FuelScheduler(4).order(item)
    assert [x["rank"] for x in vals] == list(range(1, len(vals) + 1))


def test_fcfs_score_descends():
    item = state()
    vals = FCFSScheduler(4).select(item)
    assert vals[0].score >= vals[-1].score


def test_weighted_compatible_pairs():
    item = state()
    sch = WeightedScheduler(4)
    assert len(sch.compatible_pairs(item)) == 7


def test_scheduler_waiting():
    item = state()
    assert len(FCFSScheduler(4).waiting(item)) == 4


def test_scheduler_open_runways():
    item = state()
    assert len(FCFSScheduler(4).open_runways(item)) == 2


def test_scheduler_compatibility():
    item = state()
    sch = FCFSScheduler(4)
    assert sch.compatible(item.flights[0], item.runways[0]) is True
    assert sch.compatible(item.flights[2], item.runways[0]) is False


def test_solver_time_limit():
    sch = SolverScheduler(4, time_limit=2)
    assert sch.time_limit == 2


def test_reset_last():
    item = state()
    sch = FCFSScheduler(4)
    sch.select(item)
    assert sch.last
    sch.reset()
    assert sch.last == []


def test_random_stats():
    sch = RandomScheduler(4)
    sch.select(state())
    data = sch.stats()
    assert data["name"] == "random"
    assert data["calls"] == 1


def test_fuel_stats():
    sch = FuelScheduler(4)
    sch.select(state())
    data = sch.stats()
    assert data["name"] == "fuel"
    assert data["picks"] == 2


def test_weighted_stats():
    sch = WeightedScheduler(4)
    sch.select(state())
    data = sch.stats()
    assert data["name"] == "weighted"
    assert len(data["last"]) == 2
