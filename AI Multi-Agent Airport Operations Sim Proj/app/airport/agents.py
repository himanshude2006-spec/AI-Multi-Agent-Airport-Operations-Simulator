from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Any

from app.other.types import Flight, FlightStatus, Runway, RunwayStatus, Gate, GateStatus, SimState, SimConfig, Weather, get_aircraft


@dataclass
class AgentResult:
    ok: bool
    name: str
    text: str
    data: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "name": self.name, "text": self.text, "data": self.data}


class FlightAgent:
    def __init__(self, flight: Flight) -> None:
        self.flight = flight
        self.last_action = ""
        self.action_count = 0
        self.errors = 0

    def status(self) -> str:
        return self.flight.status.value

    def is_ready(self, tick: int) -> bool:
        return self.flight.arrival_tick <= tick and self.flight.status == FlightStatus.PLANNED

    def arrive(self, tick: int) -> AgentResult:
        if not self.is_ready(tick):
            return AgentResult(False, "arrive", "flight is not ready", {"flight_id": self.flight.id})
        self.flight.mark(FlightStatus.APPROACHING, tick)
        self.last_action = "arrive"
        self.action_count += 1
        return AgentResult(True, "arrive", "flight entered airport area", {"flight_id": self.flight.id})

    def request_landing(self, tick: int) -> AgentResult:
        if self.flight.status not in {FlightStatus.APPROACHING, FlightStatus.HOLDING}:
            return AgentResult(False, "request_landing", "flight cannot request landing", {"flight_id": self.flight.id})
        self.flight.mark(FlightStatus.HOLDING, tick)
        self.last_action = "request_landing"
        self.action_count += 1
        return AgentResult(True, "request_landing", "flight requested landing", {"flight_id": self.flight.id})

    def burn_holding_fuel(self, amount: float, tick: int) -> AgentResult:
        if self.flight.status not in {FlightStatus.APPROACHING, FlightStatus.HOLDING}:
            return AgentResult(False, "burn_holding_fuel", "flight is not holding", {"flight_id": self.flight.id})
        used = self.flight.use_fuel(amount)
        self.flight.wait_ticks += 1
        self.flight.delay_ticks = max(self.flight.delay_ticks, self.flight.planned_delay(tick))
        self.last_action = "burn_holding_fuel"
        self.action_count += 1
        return AgentResult(True, "burn_holding_fuel", "holding fuel used", {"flight_id": self.flight.id, "used": used, "fuel": self.flight.fuel})

    def assign_runway(self, runway: Runway, tick: int, landing_ticks: int) -> AgentResult:
        if not runway.can_take(self.flight):
            return AgentResult(False, "assign_runway", "runway cannot take flight", {"flight_id": self.flight.id, "runway_id": runway.id})
        self.flight.runway_id = runway.id
        self.flight.landing_left = max(1, landing_ticks)
        self.flight.mark(FlightStatus.LANDING, tick)
        self.last_action = "assign_runway"
        self.action_count += 1
        return AgentResult(True, "assign_runway", "runway assigned", {"flight_id": self.flight.id, "runway_id": runway.id, "landing_ticks": landing_ticks})

    def landing_tick(self, tick: int, fuel_cost: float) -> AgentResult:
        if self.flight.status != FlightStatus.LANDING:
            return AgentResult(False, "landing_tick", "flight is not landing", {"flight_id": self.flight.id})
        self.flight.use_fuel(fuel_cost)
        self.flight.landing_left = max(0, self.flight.landing_left - 1)
        self.last_action = "landing_tick"
        self.action_count += 1
        done = self.flight.landing_left <= 0
        return AgentResult(True, "landing_tick", "landing progressed", {"flight_id": self.flight.id, "done": done, "fuel": self.flight.fuel})

    def land(self, tick: int) -> AgentResult:
        if self.flight.status != FlightStatus.LANDING:
            return AgentResult(False, "land", "flight is not landing", {"flight_id": self.flight.id})
        self.flight.landed_tick = tick
        self.flight.taxi_left = 2
        self.flight.mark(FlightStatus.TAXIING, tick)
        self.last_action = "land"
        self.action_count += 1
        return AgentResult(True, "land", "flight landed", {"flight_id": self.flight.id, "tick": tick})

    def taxi_tick(self, tick: int, fuel_cost: float) -> AgentResult:
        if self.flight.status != FlightStatus.TAXIING:
            return AgentResult(False, "taxi_tick", "flight is not taxiing", {"flight_id": self.flight.id})
        self.flight.use_fuel(fuel_cost)
        self.flight.taxi_left = max(0, self.flight.taxi_left - 1)
        self.last_action = "taxi_tick"
        self.action_count += 1
        return AgentResult(True, "taxi_tick", "taxi progressed", {"flight_id": self.flight.id, "done": self.flight.taxi_left <= 0})

    def assign_gate(self, gate: Gate, tick: int, gate_ticks: int) -> AgentResult:
        if not gate.can_take(self.flight):
            return AgentResult(False, "assign_gate", "gate cannot take flight", {"flight_id": self.flight.id, "gate_id": gate.id})
        self.flight.gate_id = gate.id
        self.flight.gate_left = max(1, gate_ticks)
        self.flight.mark(FlightStatus.AT_GATE, tick)
        self.last_action = "assign_gate"
        self.action_count += 1
        return AgentResult(True, "assign_gate", "gate assigned", {"flight_id": self.flight.id, "gate_id": gate.id, "gate_ticks": gate_ticks})

    def gate_tick(self, tick: int) -> AgentResult:
        if self.flight.status != FlightStatus.AT_GATE:
            return AgentResult(False, "gate_tick", "flight is not at gate", {"flight_id": self.flight.id})
        self.flight.gate_left = max(0, self.flight.gate_left - 1)
        self.last_action = "gate_tick"
        self.action_count += 1
        return AgentResult(True, "gate_tick", "gate work progressed", {"flight_id": self.flight.id, "done": self.flight.gate_left <= 0})

    def complete(self, tick: int) -> AgentResult:
        if self.flight.status != FlightStatus.AT_GATE:
            return AgentResult(False, "complete", "flight is not at gate", {"flight_id": self.flight.id})
        self.flight.completed_tick = tick
        self.flight.mark(FlightStatus.COMPLETED, tick)
        self.last_action = "complete"
        self.action_count += 1
        return AgentResult(True, "complete", "flight completed", {"flight_id": self.flight.id, "tick": tick})

    def divert(self, tick: int, reason: str) -> AgentResult:
        if self.flight.is_done():
            return AgentResult(False, "divert", "flight is already done", {"flight_id": self.flight.id})
        self.flight.diverted_tick = tick
        self.flight.runway_id = None
        self.flight.gate_id = None
        self.flight.add_note(reason)
        self.flight.mark(FlightStatus.DIVERTED, tick)
        self.last_action = "divert"
        self.action_count += 1
        return AgentResult(True, "divert", "flight diverted", {"flight_id": self.flight.id, "reason": reason})

    def cancel(self, tick: int, reason: str) -> AgentResult:
        if self.flight.is_done():
            return AgentResult(False, "cancel", "flight is already done", {"flight_id": self.flight.id})
        self.flight.add_note(reason)
        self.flight.mark(FlightStatus.CANCELLED, tick)
        self.last_action = "cancel"
        self.action_count += 1
        return AgentResult(True, "cancel", "flight cancelled", {"flight_id": self.flight.id, "reason": reason})

    def set_emergency(self, tick: int, reason: str) -> AgentResult:
        if self.flight.is_done():
            return AgentResult(False, "set_emergency", "flight is already done", {"flight_id": self.flight.id})
        self.flight.emergency = True
        self.flight.add_note(reason)
        self.flight.add_history(tick, "emergency", {"reason": reason})
        self.last_action = "set_emergency"
        self.action_count += 1
        return AgentResult(True, "set_emergency", "flight marked emergency", {"flight_id": self.flight.id, "reason": reason})

    def clear_emergency(self, tick: int) -> AgentResult:
        old = self.flight.emergency
        self.flight.emergency = False
        self.flight.add_history(tick, "emergency_cleared")
        self.last_action = "clear_emergency"
        self.action_count += 1
        return AgentResult(True, "clear_emergency", "emergency cleared", {"flight_id": self.flight.id, "was_emergency": old})

    def fuel_level(self, config: SimConfig) -> str:
        if self.flight.fuel <= config.diversion_fuel:
            return "divert"
        if self.flight.fuel <= config.critical_fuel:
            return "critical"
        if self.flight.fuel <= config.low_fuel:
            return "low"
        return "normal"

    def decision(self, state: SimState) -> dict[str, Any]:
        level = self.fuel_level(state.config)
        out = {"flight_id": self.flight.id, "status": self.flight.status.value, "fuel": self.flight.fuel, "fuel_level": level, "action": "wait"}
        if self.flight.status == FlightStatus.PLANNED and self.is_ready(state.tick):
            out["action"] = "arrive"
        elif level == "divert" and self.flight.is_air():
            out["action"] = "divert"
        elif self.flight.emergency and self.flight.is_waiting():
            out["action"] = "request_priority"
        elif self.flight.status == FlightStatus.APPROACHING:
            out["action"] = "request_landing"
        elif self.flight.status == FlightStatus.TAXIING and self.flight.taxi_left <= 0:
            out["action"] = "request_gate"
        elif self.flight.status == FlightStatus.AT_GATE and self.flight.gate_left <= 0:
            out["action"] = "complete"
        return out

    def info(self) -> dict[str, Any]:
        return {"flight": self.flight.to_dict(), "last_action": self.last_action, "action_count": self.action_count, "errors": self.errors}


class RunwayAgent:
    def __init__(self, runway: Runway) -> None:
        self.runway = runway
        self.last_action = ""
        self.action_count = 0
        self.rejects = 0

    def can_take(self, flight: Flight) -> bool:
        return self.runway.can_take(flight)

    def check(self, flight: Flight) -> AgentResult:
        if self.runway.status != RunwayStatus.OPEN:
            self.rejects += 1
            return AgentResult(False, "check", "runway not open", {"runway_id": self.runway.id, "flight_id": flight.id})
        if self.runway.busy_left > 0:
            self.rejects += 1
            return AgentResult(False, "check", "runway busy", {"runway_id": self.runway.id, "flight_id": flight.id})
        if self.runway.length < flight.runway_need:
            self.rejects += 1
            return AgentResult(False, "check", "runway too short", {"runway_id": self.runway.id, "flight_id": flight.id, "need": flight.runway_need, "length": self.runway.length})
        return AgentResult(True, "check", "runway accepted flight", {"runway_id": self.runway.id, "flight_id": flight.id})

    def assign(self, flight: Flight, ticks: int, tick: int) -> AgentResult:
        check = self.check(flight)
        if not check.ok:
            return check
        self.runway.assign(flight, ticks, tick)
        self.last_action = "assign"
        self.action_count += 1
        return AgentResult(True, "assign", "flight assigned to runway", {"runway_id": self.runway.id, "flight_id": flight.id, "ticks": ticks})

    def tick(self, tick: int) -> AgentResult:
        if self.runway.status == RunwayStatus.BUSY:
            self.runway.busy_ticks += 1
            self.runway.busy_left = max(0, self.runway.busy_left - 1)
            done = self.runway.busy_left <= 0
            self.last_action = "tick"
            self.action_count += 1
            return AgentResult(True, "tick", "runway busy tick", {"runway_id": self.runway.id, "done": done, "flight_id": self.runway.flight_id})
        if self.runway.status in {RunwayStatus.CLOSED, RunwayStatus.INSPECTION}:
            self.runway.closed_ticks += 1
        return AgentResult(True, "tick", "runway idle tick", {"runway_id": self.runway.id, "done": False})

    def release(self, tick: int) -> AgentResult:
        flight_id = self.runway.release(tick)
        if flight_id:
            self.runway.landings += 1
        self.last_action = "release"
        self.action_count += 1
        return AgentResult(True, "release", "runway released", {"runway_id": self.runway.id, "flight_id": flight_id})

    def close(self, tick: int, until: int = 0, reason: str = "closed") -> AgentResult:
        if self.runway.status == RunwayStatus.BUSY:
            return AgentResult(False, "close", "busy runway cannot close", {"runway_id": self.runway.id})
        self.runway.close(tick, reason)
        self.runway.failed_until = max(until, tick + 1)
        self.last_action = "close"
        self.action_count += 1
        return AgentResult(True, "close", "runway closed", {"runway_id": self.runway.id, "until": self.runway.failed_until, "reason": reason})

    def open(self, tick: int) -> AgentResult:
        if self.runway.busy_left > 0:
            return AgentResult(False, "open", "busy runway cannot open", {"runway_id": self.runway.id})
        self.runway.failed_until = 0
        self.runway.open(tick)
        self.last_action = "open"
        self.action_count += 1
        return AgentResult(True, "open", "runway opened", {"runway_id": self.runway.id})

    def inspect(self, tick: int, until: int) -> AgentResult:
        if self.runway.status == RunwayStatus.BUSY:
            return AgentResult(False, "inspect", "busy runway cannot enter inspection", {"runway_id": self.runway.id})
        self.runway.status = RunwayStatus.INSPECTION
        self.runway.failed_until = until
        self.runway.history.append({"tick": tick, "name": "inspection", "until": until})
        self.last_action = "inspect"
        self.action_count += 1
        return AgentResult(True, "inspect", "runway inspection started", {"runway_id": self.runway.id, "until": until})

    def maybe_reopen(self, tick: int) -> AgentResult:
        if self.runway.status not in {RunwayStatus.CLOSED, RunwayStatus.INSPECTION}:
            return AgentResult(False, "maybe_reopen", "runway is not closed", {"runway_id": self.runway.id})
        if tick < self.runway.failed_until:
            return AgentResult(False, "maybe_reopen", "runway closure time remains", {"runway_id": self.runway.id, "until": self.runway.failed_until})
        return self.open(tick)

    def fit_score(self, flight: Flight) -> float:
        if not self.can_take(flight):
            return -1.0
        extra = self.runway.length - flight.runway_need
        return round(100.0 - min(90.0, extra / 50.0), 3)

    def info(self, total_ticks: int) -> dict[str, Any]:
        return {"runway": self.runway.to_dict(), "utilization": self.runway.use_rate(total_ticks), "last_action": self.last_action, "action_count": self.action_count, "rejects": self.rejects}


class GateAgent:
    def __init__(self, gate: Gate) -> None:
        self.gate = gate
        self.last_action = ""
        self.action_count = 0
        self.rejects = 0

    def can_take(self, flight: Flight) -> bool:
        return self.gate.can_take(flight)

    def check(self, flight: Flight) -> AgentResult:
        if self.gate.status != GateStatus.OPEN:
            self.rejects += 1
            return AgentResult(False, "check", "gate not open", {"gate_id": self.gate.id, "flight_id": flight.id})
        if self.gate.busy_left > 0:
            self.rejects += 1
            return AgentResult(False, "check", "gate busy", {"gate_id": self.gate.id, "flight_id": flight.id})
        if flight.category not in self.gate.categories:
            self.rejects += 1
            return AgentResult(False, "check", "gate category mismatch", {"gate_id": self.gate.id, "flight_id": flight.id, "category": flight.category})
        return AgentResult(True, "check", "gate accepted flight", {"gate_id": self.gate.id, "flight_id": flight.id})

    def assign(self, flight: Flight, ticks: int, tick: int) -> AgentResult:
        check = self.check(flight)
        if not check.ok:
            return check
        self.gate.assign(flight, ticks, tick)
        self.last_action = "assign"
        self.action_count += 1
        return AgentResult(True, "assign", "flight assigned to gate", {"gate_id": self.gate.id, "flight_id": flight.id, "ticks": ticks})

    def tick(self, tick: int) -> AgentResult:
        if self.gate.status == GateStatus.BUSY:
            self.gate.busy_ticks += 1
            self.gate.busy_left = max(0, self.gate.busy_left - 1)
            done = self.gate.busy_left <= 0
            self.last_action = "tick"
            self.action_count += 1
            return AgentResult(True, "tick", "gate busy tick", {"gate_id": self.gate.id, "done": done, "flight_id": self.gate.flight_id})
        if self.gate.status == GateStatus.CLOSED:
            self.gate.closed_ticks += 1
        return AgentResult(True, "tick", "gate idle tick", {"gate_id": self.gate.id, "done": False})

    def release(self, tick: int) -> AgentResult:
        flight_id = self.gate.release(tick)
        self.last_action = "release"
        self.action_count += 1
        return AgentResult(True, "release", "gate released", {"gate_id": self.gate.id, "flight_id": flight_id})

    def close(self, tick: int, reason: str = "closed") -> AgentResult:
        if self.gate.status == GateStatus.BUSY:
            return AgentResult(False, "close", "busy gate cannot close", {"gate_id": self.gate.id})
        self.gate.close(tick)
        self.gate.history.append({"tick": tick, "name": reason})
        self.last_action = "close"
        self.action_count += 1
        return AgentResult(True, "close", "gate closed", {"gate_id": self.gate.id, "reason": reason})

    def open(self, tick: int) -> AgentResult:
        self.gate.open(tick)
        self.last_action = "open"
        self.action_count += 1
        return AgentResult(True, "open", "gate opened", {"gate_id": self.gate.id})

    def fit_score(self, flight: Flight) -> float:
        if not self.can_take(flight):
            return -1.0
        size = len(self.gate.categories)
        exact = 1 if flight.category in self.gate.categories else 0
        return round(100.0 + exact * 20.0 - size * 2.0, 3)

    def info(self, total_ticks: int) -> dict[str, Any]:
        return {"gate": self.gate.to_dict(), "utilization": self.gate.use_rate(total_ticks), "last_action": self.last_action, "action_count": self.action_count, "rejects": self.rejects}


class AirportAgent:
    def __init__(self, state: SimState) -> None:
        self.state = state
        self.flights: dict[str, FlightAgent] = {x.id: FlightAgent(x) for x in state.flights}
        self.runways: dict[str, RunwayAgent] = {x.id: RunwayAgent(x) for x in state.runways}
        self.gates: dict[str, GateAgent] = {x.id: GateAgent(x) for x in state.gates}
        self.random = random.Random(state.config.seed + 99)
        self.steps = 0
        self.errors = 0

    def rebuild(self) -> None:
        self.flights = {x.id: self.flights.get(x.id, FlightAgent(x)) for x in self.state.flights}
        self.runways = {x.id: self.runways.get(x.id, RunwayAgent(x)) for x in self.state.runways}
        self.gates = {x.id: self.gates.get(x.id, GateAgent(x)) for x in self.state.gates}
        for x in self.state.flights:
            self.flights[x.id].flight = x
        for x in self.state.runways:
            self.runways[x.id].runway = x
        for x in self.state.gates:
            self.gates[x.id].gate = x

    def flight(self, flight_id: str) -> FlightAgent | None:
        return self.flights.get(flight_id)

    def runway(self, runway_id: str) -> RunwayAgent | None:
        return self.runways.get(runway_id)

    def gate(self, gate_id: str) -> GateAgent | None:
        return self.gates.get(gate_id)

    def add_flight(self, flight: Flight) -> FlightAgent:
        self.state.flights.append(flight)
        item = FlightAgent(flight)
        self.flights[flight.id] = item
        return item

    def add_runway(self, runway: Runway) -> RunwayAgent:
        self.state.runways.append(runway)
        item = RunwayAgent(runway)
        self.runways[runway.id] = item
        return item

    def add_gate(self, gate: Gate) -> GateAgent:
        self.state.gates.append(gate)
        item = GateAgent(gate)
        self.gates[gate.id] = item
        return item

    def remove_flight(self, flight_id: str) -> bool:
        item = self.state.flight(flight_id)
        if item is None or not item.is_done():
            return False
        self.state.flights = [x for x in self.state.flights if x.id != flight_id]
        self.flights.pop(flight_id, None)
        return True

    def remove_runway(self, runway_id: str) -> bool:
        item = self.state.runway(runway_id)
        if item is None or item.status == RunwayStatus.BUSY:
            return False
        self.state.runways = [x for x in self.state.runways if x.id != runway_id]
        self.runways.pop(runway_id, None)
        return True

    def remove_gate(self, gate_id: str) -> bool:
        item = self.state.gate(gate_id)
        if item is None or item.status == GateStatus.BUSY:
            return False
        self.state.gates = [x for x in self.state.gates if x.id != gate_id]
        self.gates.pop(gate_id, None)
        return True

    def waiting_flights(self) -> list[FlightAgent]:
        return [self.flights[x.id] for x in self.state.flights if x.is_waiting()]

    def open_runways(self) -> list[RunwayAgent]:
        return [self.runways[x.id] for x in self.state.runways if x.is_open()]

    def open_gates(self) -> list[GateAgent]:
        return [self.gates[x.id] for x in self.state.gates if x.is_open()]

    def matching_runways(self, flight: Flight) -> list[RunwayAgent]:
        vals = [x for x in self.open_runways() if x.can_take(flight)]
        vals.sort(key=lambda x: (x.runway.length - flight.runway_need, x.runway.id))
        return vals

    def matching_gates(self, flight: Flight) -> list[GateAgent]:
        vals = [x for x in self.open_gates() if x.can_take(flight)]
        vals.sort(key=lambda x: (-x.fit_score(flight), x.gate.id))
        return vals

    def choose_runway(self, flight: Flight) -> RunwayAgent | None:
        vals = self.matching_runways(flight)
        return vals[0] if vals else None

    def choose_gate(self, flight: Flight) -> GateAgent | None:
        vals = self.matching_gates(flight)
        return vals[0] if vals else None

    def decisions(self) -> list[dict[str, Any]]:
        return [self.flights[x.id].decision(self.state) for x in self.state.flights if not x.is_done()]

    def emergency_candidates(self) -> list[Flight]:
        vals = [x for x in self.state.flights if x.is_waiting() and (x.emergency or x.fuel <= self.state.config.critical_fuel)]
        vals.sort(key=lambda x: (not x.emergency, x.fuel, -x.wait_ticks))
        return vals

    def low_fuel_candidates(self) -> list[Flight]:
        vals = [x for x in self.state.flights if x.is_waiting() and x.fuel <= self.state.config.low_fuel]
        vals.sort(key=lambda x: (x.fuel, -x.wait_ticks))
        return vals

    def gate_waiting(self) -> list[Flight]:
        vals = [x for x in self.state.flights if x.status == FlightStatus.TAXIING and x.taxi_left <= 0 and x.gate_id is None]
        vals.sort(key=lambda x: (x.landed_tick or 0, -x.passengers))
        return vals

    def runway_busy(self) -> list[Runway]:
        return [x for x in self.state.runways if x.status == RunwayStatus.BUSY]

    def gate_busy(self) -> list[Gate]:
        return [x for x in self.state.gates if x.status == GateStatus.BUSY]

    def status_counts(self) -> dict[str, int]:
        out = {x.value: 0 for x in FlightStatus}
        for flight in self.state.flights:
            out[flight.status.value] += 1
        return out

    def resource_counts(self) -> dict[str, Any]:
        return {
            "runways": {x.value: sum(1 for r in self.state.runways if r.status == x) for x in RunwayStatus},
            "gates": {x.value: sum(1 for g in self.state.gates if g.status == x) for x in GateStatus},
        }

    def airport_info(self) -> dict[str, Any]:
        return {
            "sim_id": self.state.id,
            "tick": self.state.tick,
            "flight_counts": self.status_counts(),
            "resource_counts": self.resource_counts(),
            "weather": self.state.weather.to_dict(),
            "steps": self.steps,
            "errors": self.errors,
        }

    def full_info(self) -> dict[str, Any]:
        return {
            "airport": self.airport_info(),
            "flights": [x.info() for x in self.flights.values()],
            "runways": [x.info(self.state.tick) for x in self.runways.values()],
            "gates": [x.info(self.state.tick) for x in self.gates.values()],
        }

    def check_state(self) -> list[str]:
        out = []
        flight_ids = {x.id for x in self.state.flights}
        runway_ids = {x.id for x in self.state.runways}
        gate_ids = {x.id for x in self.state.gates}
        for flight in self.state.flights:
            if flight.runway_id and flight.runway_id not in runway_ids:
                out.append(f"flight {flight.id} has missing runway")
            if flight.gate_id and flight.gate_id not in gate_ids:
                out.append(f"flight {flight.id} has missing gate")
        for runway in self.state.runways:
            if runway.flight_id and runway.flight_id not in flight_ids:
                out.append(f"runway {runway.id} has missing flight")
        for gate in self.state.gates:
            if gate.flight_id and gate.flight_id not in flight_ids:
                out.append(f"gate {gate.id} has missing flight")
        return out

    def repair_state(self) -> list[str]:
        out = []
        flight_ids = {x.id for x in self.state.flights}
        runway_ids = {x.id for x in self.state.runways}
        gate_ids = {x.id for x in self.state.gates}
        for flight in self.state.flights:
            if flight.runway_id and flight.runway_id not in runway_ids:
                flight.runway_id = None
                out.append(f"cleared runway from {flight.id}")
            if flight.gate_id and flight.gate_id not in gate_ids:
                flight.gate_id = None
                out.append(f"cleared gate from {flight.id}")
        for runway in self.state.runways:
            if runway.flight_id and runway.flight_id not in flight_ids:
                runway.release(self.state.tick)
                out.append(f"released {runway.id}")
        for gate in self.state.gates:
            if gate.flight_id and gate.flight_id not in flight_ids:
                gate.release(self.state.tick)
                out.append(f"released {gate.id}")
        self.rebuild()
        return out

    def random_emergency(self) -> Flight | None:
        vals = [x for x in self.state.flights if x.is_air() and not x.is_done() and not x.emergency]
        if not vals:
            return None
        return self.random.choice(vals)

    def aircraft_summary(self) -> dict[str, Any]:
        out: dict[str, dict[str, int]] = {}
        for flight in self.state.flights:
            info = get_aircraft(flight.aircraft)
            if info.category not in out:
                out[info.category] = {"flights": 0, "passengers": 0, "runway_need": 0}
            out[info.category]["flights"] += 1
            out[info.category]["passengers"] += flight.passengers
            out[info.category]["runway_need"] += flight.runway_need
        return out
