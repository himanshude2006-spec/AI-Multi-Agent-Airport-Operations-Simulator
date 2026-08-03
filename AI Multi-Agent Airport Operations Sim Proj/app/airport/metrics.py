from __future__ import annotations

import math
from dataclasses import dataclass, asdict
from statistics import mean, median
from typing import Any

from app.other.types import EventKind, Flight, FlightStatus, SimMetrics, SimState
from app.airport.schedule import airline_fairness, wait_fairness, jain_score


@dataclass
class MetricWeights:
    delay: float = 0.30
    safety: float = 0.30
    throughput: float = 0.15
    resources: float = 0.15
    fairness: float = 0.10

    def to_dict(self) -> dict[str, float]:
        return asdict(self)

    def total(self) -> float:
        return self.delay + self.safety + self.throughput + self.resources + self.fairness

    def normalized(self) -> MetricWeights:
        total = self.total()
        if total <= 0:
            return MetricWeights()
        return MetricWeights(
            delay=self.delay / total,
            safety=self.safety / total,
            throughput=self.throughput / total,
            resources=self.resources / total,
            fairness=self.fairness / total,
        )


class MetricsMaker:
    def __init__(self, weights: MetricWeights | None = None) -> None:
        self.weights = (weights or MetricWeights()).normalized()
        self.calls = 0
        self.last: SimMetrics | None = None

    def delays(self, state: SimState) -> list[int]:
        return [x.delay_ticks for x in state.flights if x.arrival_tick <= state.tick]

    def waits(self, state: SimState) -> list[int]:
        return [x.wait_ticks for x in state.flights if x.arrival_tick <= state.tick]

    def completed(self, state: SimState) -> list[Flight]:
        return [x for x in state.flights if x.status == FlightStatus.COMPLETED]

    def landed(self, state: SimState) -> list[Flight]:
        return [x for x in state.flights if x.landed_tick is not None]

    def active(self, state: SimState) -> list[Flight]:
        return [x for x in state.flights if not x.is_done()]

    def airline_delays(self, state: SimState) -> dict[str, float]:
        vals: dict[str, list[int]] = {}
        for flight in state.flights:
            vals.setdefault(flight.airline, []).append(flight.delay_ticks)
        return {key: round(mean(items), 4) if items else 0.0 for key, items in vals.items()}

    def runway_use(self, state: SimState) -> float:
        if state.tick <= 0 or not state.runways:
            return 0.0
        total = sum(x.busy_ticks for x in state.runways)
        possible = state.tick * len(state.runways)
        return min(1.0, total / possible) if possible else 0.0

    def gate_use(self, state: SimState) -> float:
        if state.tick <= 0 or not state.gates:
            return 0.0
        total = sum(x.busy_ticks for x in state.gates)
        possible = state.tick * len(state.gates)
        return min(1.0, total / possible) if possible else 0.0

    def throughput(self, state: SimState) -> float:
        if state.tick <= 0:
            return 0.0
        return len(self.completed(state)) / state.tick

    def passenger_delay(self, state: SimState) -> int:
        return sum(x.passenger_delay() for x in state.flights)

    def emergency_count(self, state: SimState) -> int:
        return sum(1 for x in state.flights if x.emergency or "emergency" in x.notes)

    def total_fuel(self, state: SimState) -> float:
        return sum(x.fuel for x in state.flights if x.status != FlightStatus.DIVERTED)

    def average_fuel(self, state: SimState) -> float:
        vals = [x.fuel for x in state.flights if x.status != FlightStatus.DIVERTED]
        return mean(vals) if vals else 0.0

    def delay_score(self, state: SimState) -> float:
        vals = self.delays(state)
        if not vals:
            return 100.0
        avg = mean(vals)
        max_val = max(vals)
        passenger = self.passenger_delay(state)
        total_people = sum(x.passengers for x in state.flights) or 1
        passenger_avg = passenger / total_people
        penalty = avg * 1.5 + max_val * 0.35 + passenger_avg * 0.2
        return max(0.0, 100.0 - penalty)

    def safety_score(self, state: SimState) -> float:
        diverted = len([x for x in state.flights if x.status == FlightStatus.DIVERTED])
        critical = state.event_count(EventKind.FUEL_CRITICAL)
        failures = state.event_count(EventKind.RUNWAY_FAILED)
        emergencies = state.event_count(EventKind.EMERGENCY)
        low = state.event_count(EventKind.FUEL_LOW)
        penalty = diverted * 18.0 + critical * 3.0 + failures * 2.0 + emergencies * 1.0 + low * 0.3
        return max(0.0, 100.0 - penalty)

    def throughput_score(self, state: SimState) -> float:
        total = len(state.flights)
        if total <= 0:
            return 0.0
        done = len(self.completed(state))
        landed = len(self.landed(state))
        base = done / total * 80.0
        base += landed / total * 20.0
        if state.all_done() and not state.diverted():
            base += 5.0
        return min(100.0, base)

    def resource_score(self, state: SimState) -> float:
        runway = self.runway_use(state)
        gate = self.gate_use(state)
        runway_target = 0.65
        gate_target = 0.55
        runway_score = max(0.0, 100.0 - abs(runway - runway_target) * 120.0)
        gate_score = max(0.0, 100.0 - abs(gate - gate_target) * 100.0)
        closures = state.event_count(EventKind.RUNWAY_CLOSED)
        penalty = min(20.0, closures * 0.8)
        return max(0.0, (runway_score + gate_score) / 2.0 - penalty)

    def fairness_score(self, state: SimState) -> float:
        a = airline_fairness(state)
        b = wait_fairness(state)
        return max(0.0, min(100.0, (a * 0.6 + b * 0.4) * 100.0))

    def fuel_score(self, state: SimState) -> float:
        vals = [x.fuel for x in state.flights if x.landed_tick is not None or x.status == FlightStatus.COMPLETED]
        if not vals:
            return 0.0
        low = sum(1 for x in vals if x <= state.config.low_fuel)
        critical = sum(1 for x in vals if x <= state.config.critical_fuel)
        avg = mean(vals)
        score = min(100.0, avg * 1.2)
        score -= low * 1.0
        score -= critical * 3.0
        return max(0.0, score)

    def overall(self, delay: float, safety: float, throughput: float, resources: float, fairness: float) -> float:
        w = self.weights
        return delay * w.delay + safety * w.safety + throughput * w.throughput + resources * w.resources + fairness * w.fairness

    def make(self, state: SimState) -> SimMetrics:
        self.calls += 1
        delays = self.delays(state)
        waits = self.waits(state)
        completed = self.completed(state)
        diverted = [x for x in state.flights if x.status == FlightStatus.DIVERTED]
        cancelled = [x for x in state.flights if x.status == FlightStatus.CANCELLED]
        active = self.active(state)
        waiting = [x for x in state.flights if x.is_waiting()]
        delay_score = self.delay_score(state)
        safety_score = self.safety_score(state)
        throughput_score = self.throughput_score(state)
        resource_score = self.resource_score(state)
        fair_score = self.fairness_score(state)
        metrics = SimMetrics(
            total_flights=len(state.flights),
            completed=len(completed),
            diverted=len(diverted),
            cancelled=len(cancelled),
            active=len(active),
            waiting=len(waiting),
            emergencies=self.emergency_count(state),
            low_fuel_events=state.event_count(EventKind.FUEL_LOW),
            critical_fuel_events=state.event_count(EventKind.FUEL_CRITICAL),
            average_delay=mean(delays) if delays else 0.0,
            max_delay=max(delays) if delays else 0,
            min_delay=min(delays) if delays else 0,
            passenger_delay=self.passenger_delay(state),
            throughput=self.throughput(state),
            runway_utilization=self.runway_use(state),
            gate_utilization=self.gate_use(state),
            fairness=wait_fairness(state),
            airline_fairness=airline_fairness(state),
            fuel_score=self.fuel_score(state),
            delay_score=delay_score,
            safety_score=safety_score,
            resource_score=resource_score,
            overall_score=self.overall(delay_score, safety_score, throughput_score, resource_score, fair_score),
            ticks=state.tick,
            landed=len(self.landed(state)),
            average_wait=mean(waits) if waits else 0.0,
            max_wait=max(waits) if waits else 0,
            events=len(state.events),
            weather_changes=state.event_count(EventKind.WEATHER_CHANGED),
            runway_closures=state.event_count(EventKind.RUNWAY_CLOSED),
            gate_uses=sum(x.uses for x in state.gates),
            total_fuel_left=self.total_fuel(state),
            average_fuel_left=self.average_fuel(state),
            airline_delays=self.airline_delays(state),
            extra={
                "median_delay": median(delays) if delays else 0.0,
                "median_wait": median(waits) if waits else 0.0,
                "throughput_score": throughput_score,
                "fairness_score": fair_score,
                "weight_values": self.weights.to_dict(),
            },
        ).rounded()
        self.last = metrics
        return metrics

    def report(self, state: SimState) -> dict[str, Any]:
        item = self.make(state)
        return {
            "metrics": item.to_dict(),
            "flight_status": status_counts(state),
            "runways": runway_report(state),
            "gates": gate_report(state),
            "airlines": airline_report(state),
            "fuel": fuel_report(state),
            "delay": delay_report(state),
            "events": event_report(state),
        }

    def compare(self, vals: list[tuple[str, SimMetrics]]) -> dict[str, Any]:
        if not vals:
            return {"items": [], "winner": None}
        items = []
        for name, item in vals:
            items.append({"name": name, **item.to_dict()})
        ranked = sorted(items, key=lambda x: (-x["overall_score"], x["average_delay"], x["diverted"]))
        for i, item in enumerate(ranked):
            item["rank"] = i + 1
        return {"items": items, "ranking": ranked, "winner": ranked[0]["name"]}


def status_counts(state: SimState) -> dict[str, int]:
    out = {x.value: 0 for x in FlightStatus}
    for flight in state.flights:
        out[flight.status.value] += 1
    return out


def runway_report(state: SimState) -> list[dict[str, Any]]:
    out = []
    for item in state.runways:
        out.append({
            "id": item.id,
            "name": item.name,
            "length": item.length,
            "status": item.status.value,
            "landings": item.landings,
            "busy_ticks": item.busy_ticks,
            "closed_ticks": item.closed_ticks,
            "utilization": item.use_rate(state.tick),
        })
    return out


def gate_report(state: SimState) -> list[dict[str, Any]]:
    out = []
    for item in state.gates:
        out.append({
            "id": item.id,
            "name": item.name,
            "categories": item.categories,
            "status": item.status.value,
            "uses": item.uses,
            "busy_ticks": item.busy_ticks,
            "closed_ticks": item.closed_ticks,
            "utilization": item.use_rate(state.tick),
        })
    return out


def airline_report(state: SimState) -> dict[str, Any]:
    vals: dict[str, dict[str, Any]] = {}
    for flight in state.flights:
        item = vals.setdefault(flight.airline, {"flights": 0, "passengers": 0, "delays": [], "completed": 0, "diverted": 0, "fuel": []})
        item["flights"] += 1
        item["passengers"] += flight.passengers
        item["delays"].append(flight.delay_ticks)
        item["fuel"].append(flight.fuel)
        if flight.status == FlightStatus.COMPLETED:
            item["completed"] += 1
        if flight.status == FlightStatus.DIVERTED:
            item["diverted"] += 1
    out = {}
    for key, item in vals.items():
        out[key] = {
            "flights": item["flights"],
            "passengers": item["passengers"],
            "average_delay": round(mean(item["delays"]), 4) if item["delays"] else 0.0,
            "max_delay": max(item["delays"]) if item["delays"] else 0,
            "completed": item["completed"],
            "diverted": item["diverted"],
            "average_fuel": round(mean(item["fuel"]), 4) if item["fuel"] else 0.0,
        }
    return out


def fuel_report(state: SimState) -> dict[str, Any]:
    vals = [x.fuel for x in state.flights]
    return {
        "average": round(mean(vals), 4) if vals else 0.0,
        "minimum": min(vals) if vals else 0.0,
        "maximum": max(vals) if vals else 0.0,
        "low": sum(1 for x in state.flights if x.fuel <= state.config.low_fuel),
        "critical": sum(1 for x in state.flights if x.fuel <= state.config.critical_fuel),
        "diversion_level": sum(1 for x in state.flights if x.fuel <= state.config.diversion_fuel),
    }


def delay_report(state: SimState) -> dict[str, Any]:
    vals = [x.delay_ticks for x in state.flights]
    waits = [x.wait_ticks for x in state.flights]
    return {
        "average": round(mean(vals), 4) if vals else 0.0,
        "median": round(median(vals), 4) if vals else 0.0,
        "maximum": max(vals) if vals else 0,
        "minimum": min(vals) if vals else 0,
        "average_wait": round(mean(waits), 4) if waits else 0.0,
        "maximum_wait": max(waits) if waits else 0,
        "passenger_delay": sum(x.passenger_delay() for x in state.flights),
    }


def event_report(state: SimState) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in state.events:
        out[item.kind.value] = out.get(item.kind.value, 0) + 1
    return out


def percentile(vals: list[float], percent: float) -> float:
    if not vals:
        return 0.0
    vals = sorted(vals)
    pos = (len(vals) - 1) * percent
    low = math.floor(pos)
    high = math.ceil(pos)
    if low == high:
        return vals[low]
    return vals[low] * (high - pos) + vals[high] * (pos - low)


def summary_table(items: list[dict[str, Any]], key: str) -> dict[str, float]:
    vals = [float(x[key]) for x in items if key in x and isinstance(x[key], (int, float))]
    return {
        "count": float(len(vals)),
        "mean": round(mean(vals), 4) if vals else 0.0,
        "median": round(median(vals), 4) if vals else 0.0,
        "min": min(vals) if vals else 0.0,
        "max": max(vals) if vals else 0.0,
        "p25": round(percentile(vals, 0.25), 4),
        "p75": round(percentile(vals, 0.75), 4),
        "p90": round(percentile(vals, 0.90), 4),
    }


def winner(items: list[tuple[str, SimMetrics]], field: str = "overall_score", high: bool = True) -> str | None:
    if not items:
        return None
    vals = sorted(items, key=lambda x: getattr(x[1], field), reverse=high)
    return vals[0][0]


metrics_maker = MetricsMaker()
