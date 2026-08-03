from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Any

from app.types import Algorithm, Flight, Runway, SimConfig, SimState

try:
    from ortools.sat.python import cp_model
except Exception:
    cp_model = None


@dataclass
class Pick:
    flight_id: str
    runway_id: str
    score: float
    reason: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "flight_id": self.flight_id,
            "runway_id": self.runway_id,
            "score": self.score,
            "reason": self.reason,
            "details": self.details,
        }


@dataclass
class ScoreParts:
    fuel: float = 0.0
    wait: float = 0.0
    emergency: float = 0.0
    passengers: float = 0.0
    size: float = 0.0
    fairness: float = 0.0
    fit: float = 0.0
    total: float = 0.0

    def to_dict(self) -> dict[str, float]:
        return {
            "fuel": round(self.fuel, 4),
            "wait": round(self.wait, 4),
            "emergency": round(self.emergency, 4),
            "passengers": round(self.passengers, 4),
            "size": round(self.size, 4),
            "fairness": round(self.fairness, 4),
            "fit": round(self.fit, 4),
            "total": round(self.total, 4),
        }


class Scheduler:
    name = "base"

    def __init__(self, seed: int = 42) -> None:
        self.seed = seed
        self.random = random.Random(seed)
        self.calls = 0
        self.picks = 0
        self.last: list[Pick] = []
        self.airline_picks: dict[str, int] = {}

    def reset(self, seed: int | None = None) -> None:
        if seed is not None:
            self.seed = seed
        self.random = random.Random(self.seed)
        self.calls = 0
        self.picks = 0
        self.last = []
        self.airline_picks = {}

    def waiting(self, state: SimState) -> list[Flight]:
        return [x for x in state.flights if x.is_waiting()]

    def open_runways(self, state: SimState) -> list[Runway]:
        return [x for x in state.runways if x.is_open()]

    def compatible(self, flight: Flight, runway: Runway) -> bool:
        return runway.can_take(flight)

    def compatible_pairs(self, state: SimState) -> list[tuple[Flight, Runway]]:
        out = []
        for flight in self.waiting(state):
            for runway in self.open_runways(state):
                if self.compatible(flight, runway):
                    out.append((flight, runway))
        return out

    def best_runway(self, flight: Flight, runways: list[Runway]) -> Runway | None:
        vals = [x for x in runways if self.compatible(flight, x)]
        vals.sort(key=lambda x: (x.length - flight.runway_need, x.name))
        return vals[0] if vals else None

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        self.last = []
        return []

    def record(self, flight: Flight, pick: Pick) -> None:
        self.picks += 1
        self.airline_picks[flight.airline] = self.airline_picks.get(flight.airline, 0) + 1
        self.last.append(pick)

    def stats(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "seed": self.seed,
            "calls": self.calls,
            "picks": self.picks,
            "airline_picks": dict(self.airline_picks),
            "last": [x.to_dict() for x in self.last],
        }

    def explain(self, state: SimState) -> dict[str, Any]:
        return {
            "algorithm": self.name,
            "waiting": len(self.waiting(state)),
            "open_runways": len(self.open_runways(state)),
            "pairs": len(self.compatible_pairs(state)),
            "stats": self.stats(),
        }


class FCFSScheduler(Scheduler):
    name = "fcfs"

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        flights = self.waiting(state)
        runways = self.open_runways(state)
        flights.sort(key=lambda x: (x.arrival_tick, x.created_tick, x.id))
        runways.sort(key=lambda x: (x.length, x.name))
        used = set()
        out = []
        for flight in flights:
            vals = [x for x in runways if x.id not in used and self.compatible(flight, x)]
            if not vals:
                continue
            runway = min(vals, key=lambda x: (x.length - flight.runway_need, x.name))
            score = 100000.0 - flight.arrival_tick * 100.0 - flight.created_tick
            pick = Pick(
                flight_id=flight.id,
                runway_id=runway.id,
                score=score,
                reason="earliest arrival",
                details={"arrival_tick": flight.arrival_tick, "wait_ticks": flight.wait_ticks},
            )
            used.add(runway.id)
            out.append(pick)
            self.record(flight, pick)
            if len(used) >= len(runways):
                break
        self.last = out
        return out

    def order(self, state: SimState) -> list[dict[str, Any]]:
        vals = self.waiting(state)
        vals.sort(key=lambda x: (x.arrival_tick, x.created_tick, x.id))
        return [{"rank": i + 1, "flight_id": x.id, "arrival_tick": x.arrival_tick, "wait_ticks": x.wait_ticks} for i, x in enumerate(vals)]


class FuelScheduler(Scheduler):
    name = "fuel"

    def fuel_score(self, flight: Flight, config: SimConfig) -> float:
        base = max(0.0, 100.0 - flight.fuel)
        if flight.fuel <= config.critical_fuel:
            base += 200.0
        elif flight.fuel <= config.low_fuel:
            base += 80.0
        if flight.emergency:
            base += 1000.0
        base += flight.wait_ticks * 0.5
        return round(base, 4)

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        flights = self.waiting(state)
        runways = self.open_runways(state)
        flights.sort(key=lambda x: (-self.fuel_score(x, state.config), x.fuel, -x.wait_ticks, x.arrival_tick))
        used = set()
        out = []
        for flight in flights:
            runway = self.best_runway(flight, [x for x in runways if x.id not in used])
            if runway is None:
                continue
            score = self.fuel_score(flight, state.config)
            pick = Pick(
                flight_id=flight.id,
                runway_id=runway.id,
                score=score,
                reason="lowest fuel first",
                details={"fuel": flight.fuel, "critical": flight.fuel <= state.config.critical_fuel, "emergency": flight.emergency},
            )
            used.add(runway.id)
            out.append(pick)
            self.record(flight, pick)
            if len(used) >= len(runways):
                break
        self.last = out
        return out

    def order(self, state: SimState) -> list[dict[str, Any]]:
        vals = self.waiting(state)
        vals.sort(key=lambda x: (-self.fuel_score(x, state.config), x.fuel, x.id))
        return [{"rank": i + 1, "flight_id": x.id, "fuel": x.fuel, "score": self.fuel_score(x, state.config)} for i, x in enumerate(vals)]


class WeightedScheduler(Scheduler):
    name = "weighted"

    def airline_delay(self, state: SimState) -> dict[str, float]:
        vals: dict[str, list[int]] = {}
        for flight in state.flights:
            vals.setdefault(flight.airline, []).append(flight.delay_ticks)
        return {key: sum(items) / len(items) if items else 0.0 for key, items in vals.items()}

    def size_value(self, flight: Flight) -> float:
        table = {"small": 1.0, "medium": 2.0, "large": 3.0, "heavy": 4.0, "super": 5.0}
        return table.get(flight.category, 2.0)

    def fit_value(self, flight: Flight, runway: Runway) -> float:
        if not self.compatible(flight, runway):
            return -10000.0
        extra = runway.length - flight.runway_need
        return max(0.0, 30.0 - extra / 100.0)

    def parts(self, flight: Flight, runway: Runway, state: SimState, airline_delay: dict[str, float] | None = None) -> ScoreParts:
        config = state.config
        vals = airline_delay or self.airline_delay(state)
        fuel = max(0.0, config.low_fuel - flight.fuel) * config.fuel_weight
        fuel += max(0.0, 100.0 - flight.fuel) * config.fuel_weight * 0.05
        if flight.fuel <= config.critical_fuel:
            fuel += config.emergency_weight * 0.8
        if flight.fuel <= config.diversion_fuel:
            fuel += config.emergency_weight * 1.5
        wait = flight.wait_ticks * config.wait_weight
        emergency = config.emergency_weight * 2.0 if flight.emergency else 0.0
        passengers = flight.passengers * config.passenger_weight
        size = self.size_value(flight) * config.size_weight
        fair = vals.get(flight.airline, 0.0) * config.fairness_weight
        pick_count = self.airline_picks.get(flight.airline, 0)
        fair -= pick_count * config.fairness_weight * 0.5
        fit = self.fit_value(flight, runway)
        total = fuel + wait + emergency + passengers + size + fair + fit
        return ScoreParts(fuel=fuel, wait=wait, emergency=emergency, passengers=passengers, size=size, fairness=fair, fit=fit, total=total)

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        flights = self.waiting(state)
        runways = self.open_runways(state)
        used_flights = set()
        used_runways = set()
        out = []
        delay = self.airline_delay(state)
        pairs = []
        for flight in flights:
            for runway in runways:
                if self.compatible(flight, runway):
                    parts = self.parts(flight, runway, state, delay)
                    pairs.append((parts.total, flight, runway, parts))
        pairs.sort(key=lambda x: (-x[0], x[1].fuel, -x[1].wait_ticks, x[1].arrival_tick, x[2].length))
        for score, flight, runway, parts in pairs:
            if flight.id in used_flights or runway.id in used_runways:
                continue
            pick = Pick(
                flight_id=flight.id,
                runway_id=runway.id,
                score=round(score, 4),
                reason="weighted priority score",
                details=parts.to_dict(),
            )
            used_flights.add(flight.id)
            used_runways.add(runway.id)
            out.append(pick)
            self.record(flight, pick)
            if len(used_runways) >= len(runways):
                break
        self.last = out
        return out

    def score_table(self, state: SimState) -> list[dict[str, Any]]:
        out = []
        delay = self.airline_delay(state)
        for flight in self.waiting(state):
            for runway in self.open_runways(state):
                if self.compatible(flight, runway):
                    parts = self.parts(flight, runway, state, delay)
                    out.append({"flight_id": flight.id, "runway_id": runway.id, "score": parts.total, "parts": parts.to_dict()})
        out.sort(key=lambda x: -x["score"])
        return out

    def order(self, state: SimState) -> list[dict[str, Any]]:
        vals = []
        delay = self.airline_delay(state)
        runways = self.open_runways(state)
        for flight in self.waiting(state):
            scores = []
            for runway in runways:
                if self.compatible(flight, runway):
                    scores.append(self.parts(flight, runway, state, delay).total)
            vals.append({"flight_id": flight.id, "score": max(scores) if scores else -1.0, "fuel": flight.fuel, "wait": flight.wait_ticks})
        vals.sort(key=lambda x: -x["score"])
        for i, item in enumerate(vals):
            item["rank"] = i + 1
        return vals


class RandomScheduler(Scheduler):
    name = "random"

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        flights = self.waiting(state)
        runways = self.open_runways(state)
        self.random.shuffle(flights)
        self.random.shuffle(runways)
        used = set()
        out = []
        for flight in flights:
            vals = [x for x in runways if x.id not in used and self.compatible(flight, x)]
            if not vals:
                continue
            runway = self.random.choice(vals)
            score = self.random.random() * 100.0
            pick = Pick(
                flight_id=flight.id,
                runway_id=runway.id,
                score=round(score, 4),
                reason="random compatible pick",
                details={"seed": self.seed},
            )
            used.add(runway.id)
            out.append(pick)
            self.record(flight, pick)
            if len(used) >= len(runways):
                break
        self.last = out
        return out


class SolverScheduler(WeightedScheduler):
    name = "solver"

    def __init__(self, seed: int = 42, time_limit: int = 3) -> None:
        super().__init__(seed)
        self.time_limit = time_limit
        self.used_solver = False
        self.solve_status = "not_run"
        self.solve_time = 0.0

    def select(self, state: SimState) -> list[Pick]:
        self.calls += 1
        if cp_model is None:
            self.solve_status = "ortools_not_installed"
            self.used_solver = False
            self.calls -= 1
            vals = super().select(state)
            for item in vals:
                item.reason = "weighted fallback because OR-Tools is not installed"
            return vals
        flights = self.waiting(state)
        runways = self.open_runways(state)
        if not flights or not runways:
            self.last = []
            self.solve_status = "empty"
            return []
        model = cp_model.CpModel()
        vars: dict[tuple[int, int], Any] = {}
        delay = self.airline_delay(state)
        for i, flight in enumerate(flights):
            for j, runway in enumerate(runways):
                if self.compatible(flight, runway):
                    vars[(i, j)] = model.NewBoolVar(f"x_{i}_{j}")
        for i in range(len(flights)):
            vals = [v for (a, b), v in vars.items() if a == i]
            if vals:
                model.Add(sum(vals) <= 1)
        for j in range(len(runways)):
            vals = [v for (a, b), v in vars.items() if b == j]
            if vals:
                model.Add(sum(vals) <= 1)
        terms = []
        scores: dict[tuple[int, int], int] = {}
        for key, var in vars.items():
            i, j = key
            score = self.parts(flights[i], runways[j], state, delay).total
            val = int(round(score * 1000))
            scores[key] = val
            terms.append(var * val)
        model.Maximize(sum(terms))
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = float(self.time_limit)
        solver.parameters.random_seed = self.seed
        status = solver.Solve(model)
        self.used_solver = True
        names = {
            cp_model.OPTIMAL: "optimal",
            cp_model.FEASIBLE: "feasible",
            cp_model.INFEASIBLE: "infeasible",
            cp_model.MODEL_INVALID: "invalid",
            cp_model.UNKNOWN: "unknown",
        }
        self.solve_status = names.get(status, str(status))
        self.solve_time = solver.WallTime()
        out = []
        if status in {cp_model.OPTIMAL, cp_model.FEASIBLE}:
            for key, var in vars.items():
                if solver.Value(var) != 1:
                    continue
                i, j = key
                flight = flights[i]
                runway = runways[j]
                parts = self.parts(flight, runway, state, delay)
                pick = Pick(
                    flight_id=flight.id,
                    runway_id=runway.id,
                    score=round(parts.total, 4),
                    reason="OR-Tools assignment",
                    details={**parts.to_dict(), "solve_status": self.solve_status, "solve_time": self.solve_time},
                )
                out.append(pick)
                self.record(flight, pick)
        out.sort(key=lambda x: -x.score)
        self.last = out
        return out

    def stats(self) -> dict[str, Any]:
        data = super().stats()
        data.update({"used_solver": self.used_solver, "solve_status": self.solve_status, "solve_time": self.solve_time, "time_limit": self.time_limit})
        return data


class SchedulerGroup:
    def __init__(self, seed: int = 42, time_limit: int = 3) -> None:
        self.seed = seed
        self.items: dict[Algorithm, Scheduler] = {
            Algorithm.FCFS: FCFSScheduler(seed),
            Algorithm.FUEL: FuelScheduler(seed),
            Algorithm.WEIGHTED: WeightedScheduler(seed),
            Algorithm.SOLVER: SolverScheduler(seed, time_limit=time_limit),
            Algorithm.RANDOM: RandomScheduler(seed),
        }

    def get(self, name: Algorithm | str) -> Scheduler:
        key = name if isinstance(name, Algorithm) else Algorithm(name)
        return self.items[key]

    def select(self, state: SimState) -> list[Pick]:
        return self.get(state.config.algorithm).select(state)

    def reset(self, seed: int | None = None) -> None:
        if seed is not None:
            self.seed = seed
        for item in self.items.values():
            item.reset(self.seed)

    def stats(self) -> dict[str, Any]:
        return {key.value: val.stats() for key, val in self.items.items()}

    def compare_current(self, state: SimState) -> dict[str, list[dict[str, Any]]]:
        out = {}
        old = {key: val.stats() for key, val in self.items.items()}
        for key, item in self.items.items():
            vals = item.select(state.copy())
            out[key.value] = [x.to_dict() for x in vals]
        for key, val in self.items.items():
            data = old[key]
            val.calls = data["calls"]
            val.picks = data["picks"]
            val.airline_picks = data["airline_picks"]
            val.last = []
        return out


def make_scheduler(name: Algorithm | str, seed: int = 42, time_limit: int = 3) -> Scheduler:
    key = name if isinstance(name, Algorithm) else Algorithm(name)
    if key == Algorithm.FCFS:
        return FCFSScheduler(seed)
    if key == Algorithm.FUEL:
        return FuelScheduler(seed)
    if key == Algorithm.WEIGHTED:
        return WeightedScheduler(seed)
    if key == Algorithm.SOLVER:
        return SolverScheduler(seed, time_limit=time_limit)
    if key == Algorithm.RANDOM:
        return RandomScheduler(seed)
    return WeightedScheduler(seed)


def algorithm_names() -> list[str]:
    return [x.value for x in Algorithm]


def compatible_count(flights: list[Flight], runways: list[Runway]) -> int:
    return sum(1 for flight in flights for runway in runways if runway.can_take(flight))


def jain_score(vals: list[float]) -> float:
    if not vals:
        return 1.0
    total = sum(vals)
    total2 = sum(x * x for x in vals)
    if total2 <= 0:
        return 1.0
    return (total * total) / (len(vals) * total2)


def airline_fairness(state: SimState) -> float:
    vals: dict[str, list[int]] = {}
    for flight in state.flights:
        vals.setdefault(flight.airline, []).append(flight.delay_ticks)
    means = [sum(x) / len(x) for x in vals.values() if x]
    if not means:
        return 1.0
    max_val = max(means)
    good = [max_val - x + 1.0 for x in means]
    return round(jain_score(good), 4)


def wait_fairness(state: SimState) -> float:
    vals = [float(x.wait_ticks + 1) for x in state.flights if x.arrival_tick <= state.tick]
    return round(jain_score(vals), 4)


def rank_flights(state: SimState, name: Algorithm | str) -> list[dict[str, Any]]:
    item = make_scheduler(name, state.config.seed)
    if isinstance(item, FCFSScheduler):
        return item.order(state)
    if isinstance(item, FuelScheduler) and not isinstance(item, WeightedScheduler):
        return item.order(state)
    if isinstance(item, WeightedScheduler):
        return item.order(state)
    vals = item.select(state.copy())
    return [{"rank": i + 1, **x.to_dict()} for i, x in enumerate(vals)]
