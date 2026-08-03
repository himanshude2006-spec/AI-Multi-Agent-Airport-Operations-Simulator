from __future__ import annotations

import asyncio
import random
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.airport.agents import AirportAgent
from app.web.events import EventBus, bus
from app.airport.metrics import MetricsMaker, metrics_maker
from app.airport.schedule import SchedulerGroup, make_scheduler
from app.other.settings import settings
from app.other.types import AIRCRAFT_CODES, Algorithm, EventKind, Experiment, ExperimentRun, Flight, FlightStatus, Gate, GateStatus, Runway, RunwayStatus, SimConfig, SimEvent, SimState, Weather, WeatherKind, get_aircraft
from app.airport.weather import WeatherMaker


def now_text() -> str:
    return datetime.now(timezone.utc).isoformat()


class SimEngine:
    def __init__(self, state: SimState, event_bus: EventBus | None = None, metrics: MetricsMaker | None = None) -> None:
        self.state = state
        self.bus = event_bus or bus
        self.metrics_maker = metrics or metrics_maker
        self.random = random.Random(state.config.seed)
        self.weather_maker = WeatherMaker(state.config.seed + 7)
        self.schedulers = SchedulerGroup(state.config.seed, time_limit=settings.solver_time_limit)
        self.airport = AirportAgent(state)
        self.lock = asyncio.Lock()
        self.running = False
        self.stop_requested = False
        self.errors: list[str] = []
        self.snapshots: list[dict[str, Any]] = []
        self.tick_times: list[float] = []

    @classmethod
    async def create(cls, config: SimConfig, event_bus: EventBus | None = None) -> SimEngine:
        problems = config.check()
        if problems:
            raise ValueError("; ".join(problems))
        state = SimState.make(config.copy())
        state.created_at = now_text()
        state.updated_at = state.created_at
        state.weather = WeatherMaker(config.seed + 7).make(config.start_weather, 0)
        item = cls(state, event_bus=event_bus)
        item.make_runways(config.runway_count)
        item.make_gates(config.gate_count)
        item.make_flights(config.flight_count)
        item.airport.rebuild()
        await item.emit(EventKind.SIM_CREATED, "simulation created", {"config": config.to_dict()})
        for flight in state.flights:
            await item.emit(EventKind.FLIGHT_CREATED, f"flight {flight.label()} created", {"flight_id": flight.id, "flight": flight.to_dict()})
        state.metrics = item.metrics_maker.make(state)
        return item

    @classmethod
    def from_state(cls, state: SimState, event_bus: EventBus | None = None) -> SimEngine:
        return cls(state.copy(), event_bus=event_bus)

    def make_runways(self, count: int) -> list[Runway]:
        lengths = [2200, 2600, 3000, 3400, 3800, 4200]
        out = []
        for i in range(count):
            length = lengths[min(i, len(lengths) - 1)]
            if i >= len(lengths):
                length += (i - len(lengths) + 1) * 200
            item = Runway(id=str(uuid4()), name=f"R{i + 1}", length=length)
            self.state.runways.append(item)
            out.append(item)
        return out

    def make_gates(self, count: int) -> list[Gate]:
        groups = [
            ["small", "medium"],
            ["small", "medium", "large"],
            ["medium", "large"],
            ["medium", "large", "heavy"],
            ["large", "heavy", "super"],
        ]
        out = []
        for i in range(count):
            cats = list(groups[i % len(groups)])
            item = Gate(id=str(uuid4()), name=f"G{i + 1}", categories=cats)
            self.state.gates.append(item)
            out.append(item)
        return out

    def make_flights(self, count: int) -> list[Flight]:
        out = []
        airlines = settings.airlines()
        origins = settings.origins()
        for i in range(count):
            code = self.random.choice(AIRCRAFT_CODES)
            info = get_aircraft(code)
            airline = self.random.choice(airlines)
            number = str(self.random.randint(100, 9999))
            passengers = self.random.randint(max(1, int(info.seats * 0.45)), max(2, info.seats))
            fuel = round(self.random.uniform(20.0, 95.0), 2)
            if self.state.config.random_arrivals:
                arrival = self.random.randint(0, self.state.config.arrival_window)
            else:
                arrival = i * 2
            emergency = self.random.random() < self.state.config.emergency_rate * 0.35
            if emergency:
                fuel = min(fuel, round(self.random.uniform(self.state.config.critical_fuel, self.state.config.low_fuel), 2))
            item = Flight(
                id=str(uuid4()),
                airline=airline,
                number=number,
                aircraft=code,
                category=info.category,
                passengers=passengers,
                fuel=fuel,
                arrival_tick=arrival,
                runway_need=info.min_runway,
                origin=self.random.choice(origins),
                emergency=emergency,
                created_tick=0,
            )
            if emergency:
                item.notes.append("initial emergency")
            self.state.flights.append(item)
            out.append(item)
        out.sort(key=lambda x: (x.arrival_tick, x.airline, x.number))
        return out

    async def emit(self, kind: EventKind, text: str, data: dict[str, Any] | None = None) -> SimEvent:
        item = SimEvent.make(self.state.id, self.state.tick, kind, text, data)
        self.state.events.append(item)
        if len(self.state.events) > settings.max_events_per_sim:
            self.state.events = self.state.events[-settings.max_events_per_sim:]
        await self.bus.publish(item)
        return item

    def flight(self, flight_id: str) -> Flight:
        item = self.state.flight(flight_id)
        if item is None:
            raise KeyError(flight_id)
        return item

    def runway(self, runway_id: str) -> Runway:
        item = self.state.runway(runway_id)
        if item is None:
            raise KeyError(runway_id)
        return item

    def gate(self, gate_id: str) -> Gate:
        item = self.state.gate(gate_id)
        if item is None:
            raise KeyError(gate_id)
        return item

    async def start(self) -> SimState:
        if self.state.status == "completed":
            return self.state
        self.state.status = "running"
        self.running = True
        self.stop_requested = False
        self.state.updated_at = now_text()
        await self.emit(EventKind.SIM_STARTED, "simulation started", {"tick": self.state.tick})
        return self.state

    async def pause(self) -> SimState:
        self.stop_requested = True
        self.running = False
        if self.state.status != "completed":
            self.state.status = "paused"
        self.state.updated_at = now_text()
        await self.emit(EventKind.SIM_PAUSED, "simulation paused", {"tick": self.state.tick})
        return self.state

    async def one_tick(self) -> SimState:
        async with self.lock:
            if self.state.status == "completed":
                return self.state
            if self.state.status == "created":
                await self.start()
            self.state.tick += 1
            self.state.updated_at = now_text()
            await self.arrivals()
            await self.random_emergencies()
            await self.weather_step()
            await self.resource_reopen_step()
            await self.fuel_step()
            await self.runway_progress_step()
            await self.gate_progress_step()
            await self.taxi_step()
            await self.assign_gates_step()
            await self.assign_runways_step()
            await self.failure_step()
            await self.check_fuel_events()
            await self.check_diversions()
            await self.finish_step()
            self.state.metrics = self.metrics_maker.make(self.state)
            await self.emit(EventKind.SIM_TICK, "simulation tick completed", self.tick_summary())
            if settings.save_snapshots and self.state.tick % max(1, settings.snapshot_gap) == 0:
                self.save_snapshot()
                await self.emit(EventKind.SNAPSHOT, "snapshot saved", {"tick": self.state.tick, "count": len(self.snapshots)})
            if self.state.all_done():
                await self.complete("all flights finished")
            elif self.state.tick >= self.state.config.max_ticks:
                await self.complete("maximum ticks reached")
            return self.state

    async def run(self, max_ticks: int | None = None) -> SimState:
        await self.start()
        limit = max_ticks if max_ticks is not None else self.state.config.max_ticks
        start_tick = self.state.tick
        while not self.stop_requested and self.state.status != "completed":
            if self.state.tick - start_tick >= limit:
                break
            await self.one_tick()
        if self.state.status != "completed" and self.state.tick >= self.state.config.max_ticks:
            await self.complete("maximum ticks reached")
        return self.state

    async def run_until(self, tick: int) -> SimState:
        if tick <= self.state.tick:
            return self.state
        while self.state.tick < tick and self.state.status != "completed" and not self.stop_requested:
            await self.one_tick()
        return self.state

    async def run_until_done(self) -> SimState:
        return await self.run(self.state.config.max_ticks)

    async def complete(self, reason: str) -> SimState:
        self.state.status = "completed"
        self.state.done_reason = reason
        self.state.updated_at = now_text()
        self.running = False
        self.stop_requested = True
        self.state.metrics = self.metrics_maker.make(self.state)
        await self.emit(EventKind.SIM_DONE, "simulation completed", {"reason": reason, "metrics": self.state.metrics.to_dict()})
        return self.state

    async def arrivals(self) -> None:
        for flight in self.state.flights:
            agent = self.airport.flight(flight.id)
            if agent is None:
                continue
            if agent.is_ready(self.state.tick):
                res = agent.arrive(self.state.tick)
                if res.ok:
                    await self.emit(EventKind.FLIGHT_ARRIVED, f"flight {flight.label()} arrived", {"flight_id": flight.id, "fuel": flight.fuel})
                    res2 = agent.request_landing(self.state.tick)
                    if res2.ok:
                        await self.emit(EventKind.LANDING_REQUESTED, f"flight {flight.label()} requested landing", {"flight_id": flight.id})

    async def random_emergencies(self) -> None:
        if not self.state.config.failures_on:
            return
        if self.random.random() >= self.state.config.emergency_rate:
            return
        flight = self.airport.random_emergency()
        if flight is None:
            return
        agent = self.airport.flight(flight.id)
        if agent is None:
            return
        reasons = ["medical problem", "hydraulic warning", "engine warning", "smoke warning", "control issue", "passenger emergency"]
        reason = self.random.choice(reasons)
        res = agent.set_emergency(self.state.tick, reason)
        if res.ok:
            await self.emit(EventKind.EMERGENCY, f"flight {flight.label()} declared emergency", {"flight_id": flight.id, "reason": reason})

    async def weather_step(self) -> None:
        if not self.state.config.weather_on:
            return
        item = self.weather_maker.maybe_change(self.state.weather, self.state.tick, self.state.config.weather_change_rate)
        if item is None:
            return
        old = self.state.weather
        self.state.weather = item
        await self.emit(EventKind.WEATHER_CHANGED, f"weather changed from {old.kind.value} to {item.kind.value}", {"old": old.to_dict(), "new": item.to_dict()})
        actions = self.weather_maker.runway_actions(item, self.state.runways, self.state.tick)
        for data in actions:
            runway = self.state.runway(data["runway_id"])
            if runway is None:
                continue
            agent = self.airport.runway(runway.id)
            if agent is None:
                continue
            if data["action"] == "close":
                res = agent.close(self.state.tick, data["until"], data["reason"])
                if res.ok:
                    item.close_count += 1
                    await self.emit(EventKind.RUNWAY_CLOSED, f"runway {runway.name} closed by weather", {"runway_id": runway.id, "until": data["until"], "weather": item.kind.value})
            elif data["action"] == "open":
                res = agent.open(self.state.tick)
                if res.ok:
                    await self.emit(EventKind.RUNWAY_OPENED, f"runway {runway.name} reopened", {"runway_id": runway.id})
        gate_actions = self.weather_maker.gate_actions(item, self.state.gates, self.state.tick)
        for data in gate_actions:
            gate = self.state.gate(data["gate_id"])
            if gate is None:
                continue
            agent = self.airport.gate(gate.id)
            if agent is None:
                continue
            res = agent.close(self.state.tick, data["reason"])
            if res.ok:
                gate.history.append({"tick": self.state.tick, "name": "closed_until", "until": data["until"]})
                await self.emit(EventKind.GATE_CLOSED, f"gate {gate.name} closed by weather", {"gate_id": gate.id, "until": data["until"]})

    async def resource_reopen_step(self) -> None:
        for runway in self.state.runways:
            if runway.status in {RunwayStatus.CLOSED, RunwayStatus.INSPECTION} and runway.failed_until <= self.state.tick:
                agent = self.airport.runway(runway.id)
                if agent is None:
                    continue
                res = agent.open(self.state.tick)
                if res.ok:
                    await self.emit(EventKind.RUNWAY_OPENED, f"runway {runway.name} opened", {"runway_id": runway.id})
        for gate in self.state.gates:
            if gate.status != GateStatus.CLOSED:
                continue
            until = 0
            for item in reversed(gate.history):
                if item.get("name") == "closed_until":
                    until = int(item.get("until", 0))
                    break
            if until and until <= self.state.tick:
                agent = self.airport.gate(gate.id)
                if agent is None:
                    continue
                res = agent.open(self.state.tick)
                if res.ok:
                    await self.emit(EventKind.GATE_OPENED, f"gate {gate.name} opened", {"gate_id": gate.id})

    async def fuel_step(self) -> None:
        for flight in self.state.flights:
            if not flight.is_waiting():
                continue
            agent = self.airport.flight(flight.id)
            if agent is None:
                continue
            info = get_aircraft(flight.aircraft)
            base = self.state.config.holding_fuel_cost * info.fuel_burn
            amount = self.weather_maker.fuel_cost(base, self.state.weather)
            agent.burn_holding_fuel(amount, self.state.tick)

    async def runway_progress_step(self) -> None:
        for runway in self.state.runways:
            agent = self.airport.runway(runway.id)
            if agent is None:
                continue
            flight_id = runway.flight_id
            res = agent.tick(self.state.tick)
            if flight_id:
                flight = self.state.flight(flight_id)
                if flight is not None and flight.status == FlightStatus.LANDING:
                    fagent = self.airport.flight(flight.id)
                    if fagent is not None:
                        info = get_aircraft(flight.aircraft)
                        cost = self.state.config.landing_fuel_cost * info.fuel_burn / max(1, flight.landing_left)
                        fagent.landing_tick(self.state.tick, cost)
                if res.data.get("done"):
                    if flight is not None:
                        fagent = self.airport.flight(flight.id)
                        if fagent is not None:
                            fagent.land(self.state.tick)
                            flight.runway_id = None
                            await self.emit(EventKind.LANDING_COMPLETED, f"flight {flight.label()} landed", {"flight_id": flight.id, "runway_id": runway.id, "fuel": flight.fuel})
                            await self.emit(EventKind.TAXI_STARTED, f"flight {flight.label()} started taxi", {"flight_id": flight.id})
                    agent.release(self.state.tick)

    async def gate_progress_step(self) -> None:
        for gate in self.state.gates:
            agent = self.airport.gate(gate.id)
            if agent is None:
                continue
            flight_id = gate.flight_id
            res = agent.tick(self.state.tick)
            if flight_id and res.data.get("done"):
                flight = self.state.flight(flight_id)
                if flight is not None:
                    fagent = self.airport.flight(flight.id)
                    if fagent is not None:
                        fagent.complete(self.state.tick)
                        flight.gate_id = None
                        await self.emit(EventKind.FLIGHT_COMPLETED, f"flight {flight.label()} completed", {"flight_id": flight.id, "gate_id": gate.id})
                agent.release(self.state.tick)
                await self.emit(EventKind.GATE_RELEASED, f"gate {gate.name} released", {"gate_id": gate.id, "flight_id": flight_id})

    async def taxi_step(self) -> None:
        for flight in self.state.flights:
            if flight.status != FlightStatus.TAXIING or flight.taxi_left <= 0:
                continue
            agent = self.airport.flight(flight.id)
            if agent is None:
                continue
            info = get_aircraft(flight.aircraft)
            agent.taxi_tick(self.state.tick, settings.taxi_fuel_cost * info.fuel_burn)

    async def assign_gates_step(self) -> None:
        for flight in self.airport.gate_waiting():
            gate_agent = self.airport.choose_gate(flight)
            if gate_agent is None:
                flight.delay_ticks += 1
                continue
            fagent = self.airport.flight(flight.id)
            if fagent is None:
                continue
            info = get_aircraft(flight.aircraft)
            base = max(self.state.config.gate_hold_time, info.gate_time)
            ticks = self.weather_maker.gate_time(base, self.state.weather)
            res1 = gate_agent.assign(flight, ticks, self.state.tick)
            res2 = fagent.assign_gate(gate_agent.gate, self.state.tick, ticks)
            if res1.ok and res2.ok:
                await self.emit(EventKind.GATE_ASSIGNED, f"flight {flight.label()} assigned gate {gate_agent.gate.name}", {"flight_id": flight.id, "gate_id": gate_agent.gate.id, "ticks": ticks})

    async def assign_runways_step(self) -> None:
        scheduler = self.schedulers.get(self.state.config.algorithm)
        picks = scheduler.select(self.state)
        for pick in picks:
            flight = self.state.flight(pick.flight_id)
            runway = self.state.runway(pick.runway_id)
            if flight is None or runway is None:
                continue
            fagent = self.airport.flight(flight.id)
            ragent = self.airport.runway(runway.id)
            if fagent is None or ragent is None:
                continue
            info = get_aircraft(flight.aircraft)
            base = self.state.config.landing_time + max(0, info.landing_size - 2)
            ticks = self.weather_maker.runway_time(base, self.state.weather) + self.state.config.runway_gap
            res1 = ragent.assign(flight, ticks, self.state.tick)
            res2 = fagent.assign_runway(runway, self.state.tick, ticks)
            if res1.ok and res2.ok:
                flight.score = pick.score
                await self.emit(EventKind.FLIGHT_SELECTED, f"flight {flight.label()} selected by {scheduler.name}", {"flight_id": flight.id, "runway_id": runway.id, "score": pick.score, "reason": pick.reason, "details": pick.details})
                await self.emit(EventKind.RUNWAY_ASSIGNED, f"runway {runway.name} assigned to flight {flight.label()}", {"flight_id": flight.id, "runway_id": runway.id, "ticks": ticks})
                await self.emit(EventKind.LANDING_STARTED, f"flight {flight.label()} started landing", {"flight_id": flight.id, "runway_id": runway.id})

    async def failure_step(self) -> None:
        if not self.state.config.failures_on:
            return
        if self.random.random() >= self.state.config.failure_rate:
            return
        vals = [x for x in self.state.runways if x.status == RunwayStatus.OPEN]
        if not vals:
            return
        runway = self.random.choice(vals)
        agent = self.airport.runway(runway.id)
        if agent is None:
            return
        until = self.state.tick + self.random.randint(3, 12)
        res = agent.inspect(self.state.tick, until)
        if res.ok:
            await self.emit(EventKind.RUNWAY_FAILED, f"runway {runway.name} entered inspection", {"runway_id": runway.id, "until": until})
            await self.emit(EventKind.RUNWAY_CLOSED, f"runway {runway.name} closed for inspection", {"runway_id": runway.id, "until": until})

    async def check_fuel_events(self) -> None:
        for flight in self.state.flights:
            if not flight.is_air() or flight.status == FlightStatus.PLANNED:
                continue
            if flight.fuel <= self.state.config.critical_fuel and not flight.critical_fuel_sent:
                flight.critical_fuel_sent = True
                await self.emit(EventKind.FUEL_CRITICAL, f"flight {flight.label()} has critical fuel", {"flight_id": flight.id, "fuel": flight.fuel})
            elif flight.fuel <= self.state.config.low_fuel and not flight.low_fuel_sent:
                flight.low_fuel_sent = True
                await self.emit(EventKind.FUEL_LOW, f"flight {flight.label()} has low fuel", {"flight_id": flight.id, "fuel": flight.fuel})

    async def check_diversions(self) -> None:
        for flight in self.state.flights:
            if not flight.is_waiting():
                continue
            if flight.fuel > self.state.config.diversion_fuel:
                continue
            agent = self.airport.flight(flight.id)
            if agent is None:
                continue
            res = agent.divert(self.state.tick, "fuel reached diversion level")
            if res.ok:
                await self.emit(EventKind.DIVERTED, f"flight {flight.label()} diverted", {"flight_id": flight.id, "fuel": flight.fuel, "reason": "low fuel"})

    async def finish_step(self) -> None:
        for flight in self.state.flights:
            if flight.status == FlightStatus.AT_GATE and flight.gate_left > 0:
                agent = self.airport.flight(flight.id)
                if agent is not None:
                    agent.gate_tick(self.state.tick)
            if flight.arrival_tick <= self.state.tick and not flight.is_done():
                flight.delay_ticks = max(flight.delay_ticks, max(0, self.state.tick - flight.arrival_tick))

    def tick_summary(self) -> dict[str, Any]:
        return {
            "tick": self.state.tick,
            "status": self.state.status,
            "waiting": len(self.state.waiting()),
            "active": len(self.state.active()),
            "done": len(self.state.done()),
            "open_runways": len(self.state.open_runways()),
            "open_gates": len(self.state.open_gates()),
            "weather": self.state.weather.to_dict(),
            "metrics": self.state.metrics.to_dict(),
        }

    def save_snapshot(self) -> dict[str, Any]:
        data = self.state.to_dict(include_events=False)
        data["snapshot_tick"] = self.state.tick
        self.snapshots.append(data)
        if len(self.snapshots) > 200:
            self.snapshots = self.snapshots[-200:]
        return data

    def get_snapshot(self, tick: int) -> dict[str, Any] | None:
        vals = [x for x in self.snapshots if x.get("snapshot_tick") == tick]
        return vals[-1] if vals else None

    def closest_snapshot(self, tick: int) -> dict[str, Any] | None:
        vals = [x for x in self.snapshots if x.get("snapshot_tick", 0) <= tick]
        vals.sort(key=lambda x: x.get("snapshot_tick", 0), reverse=True)
        return vals[0] if vals else None

    async def add_flight(self, data: dict[str, Any]) -> Flight:
        code = str(data.get("aircraft", "A320"))
        info = get_aircraft(code)
        item = Flight(
            id=str(data.get("id") or uuid4()),
            airline=str(data.get("airline", "XX")),
            number=str(data.get("number", self.random.randint(100, 9999))),
            aircraft=code,
            category=str(data.get("category", info.category)),
            passengers=int(data.get("passengers", max(1, int(info.seats * 0.7)))),
            fuel=float(data.get("fuel", 60.0)),
            arrival_tick=int(data.get("arrival_tick", self.state.tick)),
            runway_need=int(data.get("runway_need", info.min_runway)),
            origin=str(data.get("origin", "UNK")),
            emergency=bool(data.get("emergency", False)),
            created_tick=self.state.tick,
        )
        self.airport.add_flight(item)
        await self.emit(EventKind.FLIGHT_CREATED, f"flight {item.label()} added", {"flight_id": item.id, "flight": item.to_dict()})
        return item

    async def add_runway(self, data: dict[str, Any]) -> Runway:
        item = Runway(id=str(data.get("id") or uuid4()), name=str(data.get("name", f"R{len(self.state.runways) + 1}")), length=int(data.get("length", 3000)))
        self.airport.add_runway(item)
        return item

    async def add_gate(self, data: dict[str, Any]) -> Gate:
        cats = list(data.get("categories", ["small", "medium", "large"]))
        item = Gate(id=str(data.get("id") or uuid4()), name=str(data.get("name", f"G{len(self.state.gates) + 1}")), categories=cats)
        self.airport.add_gate(item)
        return item

    async def force_weather(self, kind: str, level: int | None = None) -> Weather:
        old = self.state.weather
        item = self.weather_maker.force(kind, self.state.tick, level)
        self.state.weather = item
        await self.emit(EventKind.WEATHER_CHANGED, f"weather forced from {old.kind.value} to {item.kind.value}", {"old": old.to_dict(), "new": item.to_dict(), "forced": True})
        return item

    async def close_runway(self, runway_id: str, ticks: int, reason: str) -> Runway:
        runway = self.runway(runway_id)
        agent = self.airport.runway(runway_id)
        if agent is None:
            raise KeyError(runway_id)
        res = agent.close(self.state.tick, self.state.tick + max(1, ticks), reason)
        if not res.ok:
            raise ValueError(res.text)
        await self.emit(EventKind.RUNWAY_CLOSED, f"runway {runway.name} closed", {"runway_id": runway.id, "until": runway.failed_until, "reason": reason})
        return runway

    async def open_runway(self, runway_id: str) -> Runway:
        runway = self.runway(runway_id)
        agent = self.airport.runway(runway_id)
        if agent is None:
            raise KeyError(runway_id)
        res = agent.open(self.state.tick)
        if not res.ok:
            raise ValueError(res.text)
        await self.emit(EventKind.RUNWAY_OPENED, f"runway {runway.name} opened", {"runway_id": runway.id})
        return runway

    async def mark_emergency(self, flight_id: str, reason: str) -> Flight:
        flight = self.flight(flight_id)
        agent = self.airport.flight(flight_id)
        if agent is None:
            raise KeyError(flight_id)
        res = agent.set_emergency(self.state.tick, reason)
        if not res.ok:
            raise ValueError(res.text)
        await self.emit(EventKind.EMERGENCY, f"flight {flight.label()} declared emergency", {"flight_id": flight.id, "reason": reason})
        return flight

    async def divert_flight(self, flight_id: str, reason: str) -> Flight:
        flight = self.flight(flight_id)
        agent = self.airport.flight(flight_id)
        if agent is None:
            raise KeyError(flight_id)
        res = agent.divert(self.state.tick, reason)
        if not res.ok:
            raise ValueError(res.text)
        await self.emit(EventKind.DIVERTED, f"flight {flight.label()} diverted", {"flight_id": flight.id, "reason": reason})
        return flight

    def scheduler_info(self) -> dict[str, Any]:
        item = self.schedulers.get(self.state.config.algorithm)
        return {"current": self.state.config.algorithm.value, "details": item.explain(self.state), "all": self.schedulers.stats()}

    def compare_picks(self) -> dict[str, list[dict[str, Any]]]:
        return self.schedulers.compare_current(self.state)

    def state_data(self, include_events: bool = True) -> dict[str, Any]:
        return self.state.to_dict(include_events=include_events)

    def report(self) -> dict[str, Any]:
        return self.metrics_maker.report(self.state)

    def check(self) -> list[str]:
        out = self.state.config.check()
        out.extend(self.airport.check_state())
        for flight in self.state.flights:
            if flight.fuel < 0:
                out.append(f"flight {flight.id} has negative fuel")
            if flight.passengers < 0:
                out.append(f"flight {flight.id} has negative passengers")
            if flight.runway_need <= 0:
                out.append(f"flight {flight.id} has invalid runway need")
        return out

    def repair(self) -> list[str]:
        out = self.airport.repair_state()
        for flight in self.state.flights:
            if flight.fuel < 0:
                flight.fuel = 0.0
                out.append(f"fixed fuel for {flight.id}")
            if flight.passengers < 0:
                flight.passengers = 0
                out.append(f"fixed passengers for {flight.id}")
        return out

    def clone(self, seed: int | None = None, algorithm: Algorithm | None = None) -> SimEngine:
        config = self.state.config.copy()
        if seed is not None:
            config.seed = seed
        if algorithm is not None:
            config.algorithm = algorithm
        state = self.state.copy()
        state.id = str(uuid4())
        state.config = config
        state.tick = 0
        state.status = "created"
        state.events = []
        state.metrics = self.metrics_maker.make(state)
        state.created_at = now_text()
        state.updated_at = state.created_at
        for flight in state.flights:
            flight.status = FlightStatus.PLANNED
            flight.runway_id = None
            flight.gate_id = None
            flight.wait_ticks = 0
            flight.delay_ticks = 0
            flight.landing_left = 0
            flight.taxi_left = 0
            flight.gate_left = 0
            flight.landed_tick = None
            flight.completed_tick = None
            flight.diverted_tick = None
            flight.history = []
            flight.low_fuel_sent = False
            flight.critical_fuel_sent = False
        for runway in state.runways:
            runway.status = RunwayStatus.OPEN
            runway.busy_left = 0
            runway.flight_id = None
            runway.landings = 0
            runway.busy_ticks = 0
            runway.closed_ticks = 0
            runway.failed_until = 0
            runway.history = []
        for gate in state.gates:
            gate.status = GateStatus.OPEN
            gate.busy_left = 0
            gate.flight_id = None
            gate.uses = 0
            gate.busy_ticks = 0
            gate.closed_ticks = 0
            gate.history = []
        state.weather = WeatherMaker(config.seed + 7).make(config.start_weather, 0)
        return SimEngine(state, event_bus=self.bus, metrics=self.metrics_maker)


class ExperimentRunner:
    def __init__(self, event_bus: EventBus | None = None) -> None:
        self.bus = event_bus or bus
        self.items: dict[str, Experiment] = {}
        self.engines: dict[str, SimEngine] = {}
        self.lock = asyncio.Lock()

    async def make(self, name: str, algorithms: list[Algorithm], runs: int, config: SimConfig) -> Experiment:
        item = Experiment.make(name, algorithms, runs, config.copy())
        item.created_at = now_text()
        item.updated_at = item.created_at
        self.items[item.id] = item
        return item

    async def run(self, item: Experiment) -> Experiment:
        async with self.lock:
            item.status = "running"
            item.updated_at = now_text()
            for run_number in range(1, item.runs + 1):
                seed = item.base_config.seed + run_number - 1
                for algorithm in item.algorithms:
                    config = item.base_config.copy()
                    config.seed = seed
                    config.algorithm = algorithm
                    try:
                        engine = await SimEngine.create(config, event_bus=self.bus)
                        self.engines[engine.state.id] = engine
                        await engine.run_until_done()
                        row = ExperimentRun(algorithm=algorithm, run_number=run_number, seed=seed, sim_id=engine.state.id, metrics=engine.state.metrics, status="done")
                    except Exception as exc:
                        row = ExperimentRun(algorithm=algorithm, run_number=run_number, seed=seed, sim_id="", metrics=metrics_maker.last or metrics_maker.make(SimState.make(config)), status="failed", error=str(exc))
                    item.items.append(row)
                    item.updated_at = now_text()
            item.summary = self.summarize(item)
            item.status = "completed"
            item.updated_at = now_text()
            return item

    def summarize(self, item: Experiment) -> dict[str, Any]:
        groups: dict[str, list[ExperimentRun]] = {}
        for row in item.items:
            if row.status == "done":
                groups.setdefault(row.algorithm.value, []).append(row)
        out: dict[str, Any] = {}
        for name, rows in groups.items():
            count = len(rows)
            out[name] = {
                "runs": count,
                "average_delay": round(sum(x.metrics.average_delay for x in rows) / count, 4),
                "average_score": round(sum(x.metrics.overall_score for x in rows) / count, 4),
                "average_throughput": round(sum(x.metrics.throughput for x in rows) / count, 4),
                "average_runway_utilization": round(sum(x.metrics.runway_utilization for x in rows) / count, 4),
                "average_gate_utilization": round(sum(x.metrics.gate_utilization for x in rows) / count, 4),
                "average_fairness": round(sum(x.metrics.airline_fairness for x in rows) / count, 4),
                "diversions": sum(x.metrics.diverted for x in rows),
                "emergencies": sum(x.metrics.emergencies for x in rows),
            }
        ranking = sorted(out.items(), key=lambda x: (-x[1]["average_score"], x[1]["average_delay"], x[1]["diversions"]))
        return {
            "algorithms": out,
            "ranking": [{"rank": i + 1, "algorithm": name, **data} for i, (name, data) in enumerate(ranking)],
            "winner": ranking[0][0] if ranking else None,
            "total_runs": len(item.items),
            "successful_runs": sum(1 for x in item.items if x.status == "done"),
            "failed_runs": sum(1 for x in item.items if x.status != "done"),
        }

    def get(self, experiment_id: str) -> Experiment | None:
        return self.items.get(experiment_id)

    def list(self) -> list[Experiment]:
        vals = list(self.items.values())
        vals.sort(key=lambda x: x.created_at, reverse=True)
        return vals

    def delete(self, experiment_id: str) -> bool:
        return self.items.pop(experiment_id, None) is not None


class EngineStore:
    def __init__(self) -> None:
        self.items: dict[str, SimEngine] = {}
        self.order: list[str] = []
        self.lock = asyncio.Lock()

    async def add(self, engine: SimEngine) -> SimEngine:
        async with self.lock:
            self.items[engine.state.id] = engine
            if engine.state.id in self.order:
                self.order.remove(engine.state.id)
            self.order.append(engine.state.id)
            while len(self.order) > settings.max_simulations:
                old = self.order.pop(0)
                self.items.pop(old, None)
        return engine

    async def create(self, config: SimConfig) -> SimEngine:
        engine = await SimEngine.create(config)
        await self.add(engine)
        return engine

    def get(self, sim_id: str) -> SimEngine | None:
        return self.items.get(sim_id)

    def need(self, sim_id: str) -> SimEngine:
        item = self.get(sim_id)
        if item is None:
            raise KeyError(sim_id)
        return item

    async def delete(self, sim_id: str) -> bool:
        async with self.lock:
            item = self.items.pop(sim_id, None)
            if sim_id in self.order:
                self.order.remove(sim_id)
            return item is not None

    def list(self) -> list[SimEngine]:
        return [self.items[x] for x in reversed(self.order) if x in self.items]

    def stats(self) -> dict[str, Any]:
        return {
            "count": len(self.items),
            "running": sum(1 for x in self.items.values() if x.state.status == "running"),
            "completed": sum(1 for x in self.items.values() if x.state.status == "completed"),
            "paused": sum(1 for x in self.items.values() if x.state.status == "paused"),
            "ticks": sum(x.state.tick for x in self.items.values()),
            "events": sum(len(x.state.events) for x in self.items.values()),
        }


engine_store = EngineStore()
experiment_runner = ExperimentRunner()
