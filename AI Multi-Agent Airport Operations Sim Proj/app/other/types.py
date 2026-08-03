from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any
from uuid import uuid4
import copy
import json
import math


class FlightStatus(str, Enum):
    PLANNED = "planned"
    APPROACHING = "approaching"
    HOLDING = "holding"
    LANDING = "landing"
    TAXIING = "taxiing"
    AT_GATE = "at_gate"
    COMPLETED = "completed"
    DIVERTED = "diverted"
    CANCELLED = "cancelled"


class RunwayStatus(str, Enum):
    OPEN = "open"
    BUSY = "busy"
    CLOSED = "closed"
    INSPECTION = "inspection"


class GateStatus(str, Enum):
    OPEN = "open"
    BUSY = "busy"
    CLOSED = "closed"


class WeatherKind(str, Enum):
    CLEAR = "clear"
    RAIN = "rain"
    FOG = "fog"
    STORM = "storm"
    SNOW = "snow"
    WIND = "wind"


class EventKind(str, Enum):
    SIM_CREATED = "simulation_created"
    SIM_STARTED = "simulation_started"
    SIM_TICK = "simulation_tick"
    SIM_DONE = "simulation_completed"
    SIM_PAUSED = "simulation_paused"
    FLIGHT_CREATED = "flight_created"
    FLIGHT_ARRIVED = "flight_arrived"
    LANDING_REQUESTED = "landing_requested"
    FLIGHT_SELECTED = "flight_selected"
    RUNWAY_ASSIGNED = "runway_assigned"
    LANDING_STARTED = "landing_started"
    LANDING_COMPLETED = "landing_completed"
    TAXI_STARTED = "taxi_started"
    GATE_ASSIGNED = "gate_assigned"
    GATE_RELEASED = "gate_released"
    FLIGHT_COMPLETED = "flight_completed"
    FUEL_LOW = "fuel_low"
    FUEL_CRITICAL = "fuel_critical"
    EMERGENCY = "emergency_landing"
    DIVERTED = "flight_diverted"
    WEATHER_CHANGED = "weather_changed"
    RUNWAY_CLOSED = "runway_closed"
    RUNWAY_OPENED = "runway_opened"
    RUNWAY_FAILED = "runway_failed"
    GATE_CLOSED = "gate_closed"
    GATE_OPENED = "gate_opened"
    AI_REQUESTED = "ai_requested"
    AI_RECOMMENDED = "ai_recommended"
    AI_APPLIED = "ai_applied"
    AI_REJECTED = "ai_rejected"
    SNAPSHOT = "snapshot_saved"
    ERROR = "error"


class Algorithm(str, Enum):
    FCFS = "fcfs"
    FUEL = "fuel"
    WEIGHTED = "weighted"
    SOLVER = "solver"
    RANDOM = "random"


@dataclass
class AircraftInfo:
    code: str
    name: str
    category: str
    min_runway: int
    seats: int
    fuel_burn: float
    landing_size: int
    gate_time: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AircraftInfo:
        return cls(**data)


@dataclass
class Flight:
    id: str
    airline: str
    number: str
    aircraft: str
    category: str
    passengers: int
    fuel: float
    arrival_tick: int
    runway_need: int
    origin: str = "UNK"
    status: FlightStatus = FlightStatus.PLANNED
    runway_id: str | None = None
    gate_id: str | None = None
    wait_ticks: int = 0
    delay_ticks: int = 0
    landing_left: int = 0
    taxi_left: int = 0
    gate_left: int = 0
    emergency: bool = False
    low_fuel_sent: bool = False
    critical_fuel_sent: bool = False
    created_tick: int = 0
    landed_tick: int | None = None
    completed_tick: int | None = None
    diverted_tick: int | None = None
    score: float = 0.0
    notes: list[str] = field(default_factory=list)
    history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Flight:
        x = dict(data)
        x["status"] = FlightStatus(x.get("status", FlightStatus.PLANNED.value))
        return cls(**x)

    def copy(self) -> Flight:
        return Flight.from_dict(self.to_dict())

    def add_history(self, tick: int, name: str, data: dict[str, Any] | None = None) -> None:
        self.history.append({"tick": tick, "name": name, "data": data or {}})

    def is_done(self) -> bool:
        return self.status in {FlightStatus.COMPLETED, FlightStatus.DIVERTED, FlightStatus.CANCELLED}

    def is_waiting(self) -> bool:
        return self.status in {FlightStatus.APPROACHING, FlightStatus.HOLDING}

    def is_air(self) -> bool:
        return self.status in {FlightStatus.PLANNED, FlightStatus.APPROACHING, FlightStatus.HOLDING, FlightStatus.LANDING}

    def can_land_on(self, runway: Runway) -> bool:
        return runway.length >= self.runway_need and runway.status == RunwayStatus.OPEN

    def can_use_gate(self, gate: Gate) -> bool:
        return gate.status == GateStatus.OPEN and self.category in gate.categories

    def mark(self, status: FlightStatus, tick: int) -> None:
        self.status = status
        self.add_history(tick, status.value)

    def use_fuel(self, val: float) -> float:
        old = self.fuel
        self.fuel = max(0.0, round(self.fuel - val, 3))
        return old - self.fuel

    def add_note(self, val: str) -> None:
        if val not in self.notes:
            self.notes.append(val)

    def clear_note(self, val: str) -> None:
        if val in self.notes:
            self.notes.remove(val)

    def label(self) -> str:
        return f"{self.airline}{self.number}"

    def planned_delay(self, tick: int) -> int:
        return max(0, tick - self.arrival_tick)

    def passenger_delay(self) -> int:
        return self.delay_ticks * self.passengers

    def risk(self) -> str:
        if self.emergency:
            return "emergency"
        if self.fuel <= 6:
            return "divert"
        if self.fuel <= 12:
            return "critical"
        if self.fuel <= 25:
            return "low"
        return "normal"


@dataclass
class Runway:
    id: str
    name: str
    length: int
    status: RunwayStatus = RunwayStatus.OPEN
    busy_left: int = 0
    flight_id: str | None = None
    landings: int = 0
    busy_ticks: int = 0
    closed_ticks: int = 0
    failed_until: int = 0
    history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Runway:
        x = dict(data)
        x["status"] = RunwayStatus(x.get("status", RunwayStatus.OPEN.value))
        return cls(**x)

    def copy(self) -> Runway:
        return Runway.from_dict(self.to_dict())

    def is_open(self) -> bool:
        return self.status == RunwayStatus.OPEN and self.busy_left <= 0

    def can_take(self, flight: Flight) -> bool:
        return self.is_open() and self.length >= flight.runway_need

    def assign(self, flight: Flight, ticks: int, tick: int) -> None:
        self.status = RunwayStatus.BUSY
        self.flight_id = flight.id
        self.busy_left = max(1, ticks)
        self.history.append({"tick": tick, "name": "assigned", "flight_id": flight.id})

    def release(self, tick: int) -> str | None:
        old = self.flight_id
        self.flight_id = None
        self.busy_left = 0
        if self.status == RunwayStatus.BUSY:
            self.status = RunwayStatus.OPEN
        self.history.append({"tick": tick, "name": "released", "flight_id": old})
        return old

    def close(self, tick: int, name: str = "closed") -> None:
        self.status = RunwayStatus.CLOSED
        self.history.append({"tick": tick, "name": name})

    def open(self, tick: int) -> None:
        if self.busy_left > 0:
            self.status = RunwayStatus.BUSY
        else:
            self.status = RunwayStatus.OPEN
        self.history.append({"tick": tick, "name": "opened"})

    def use_rate(self, ticks: int) -> float:
        if ticks <= 0:
            return 0.0
        return round(self.busy_ticks / ticks, 4)


@dataclass
class Gate:
    id: str
    name: str
    categories: list[str]
    status: GateStatus = GateStatus.OPEN
    busy_left: int = 0
    flight_id: str | None = None
    uses: int = 0
    busy_ticks: int = 0
    closed_ticks: int = 0
    history: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Gate:
        x = dict(data)
        x["status"] = GateStatus(x.get("status", GateStatus.OPEN.value))
        return cls(**x)

    def copy(self) -> Gate:
        return Gate.from_dict(self.to_dict())

    def is_open(self) -> bool:
        return self.status == GateStatus.OPEN and self.busy_left <= 0

    def can_take(self, flight: Flight) -> bool:
        return self.is_open() and flight.category in self.categories

    def assign(self, flight: Flight, ticks: int, tick: int) -> None:
        self.status = GateStatus.BUSY
        self.flight_id = flight.id
        self.busy_left = max(1, ticks)
        self.uses += 1
        self.history.append({"tick": tick, "name": "assigned", "flight_id": flight.id})

    def release(self, tick: int) -> str | None:
        old = self.flight_id
        self.flight_id = None
        self.busy_left = 0
        if self.status == GateStatus.BUSY:
            self.status = GateStatus.OPEN
        self.history.append({"tick": tick, "name": "released", "flight_id": old})
        return old

    def close(self, tick: int) -> None:
        self.status = GateStatus.CLOSED
        self.history.append({"tick": tick, "name": "closed"})

    def open(self, tick: int) -> None:
        if self.busy_left > 0:
            self.status = GateStatus.BUSY
        else:
            self.status = GateStatus.OPEN
        self.history.append({"tick": tick, "name": "opened"})

    def use_rate(self, ticks: int) -> float:
        if ticks <= 0:
            return 0.0
        return round(self.busy_ticks / ticks, 4)


@dataclass
class Weather:
    kind: WeatherKind = WeatherKind.CLEAR
    level: int = 0
    wind: int = 4
    visibility: int = 10
    temp: int = 20
    changed_tick: int = 0
    runway_slow: float = 0.0
    gate_slow: float = 0.0
    fuel_slow: float = 0.0
    close_count: int = 0
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["kind"] = self.kind.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Weather:
        x = dict(data)
        x["kind"] = WeatherKind(x.get("kind", WeatherKind.CLEAR.value))
        return cls(**x)

    def copy(self) -> Weather:
        return Weather.from_dict(self.to_dict())

    def is_bad(self) -> bool:
        return self.kind != WeatherKind.CLEAR and self.level >= 2

    def is_dangerous(self) -> bool:
        return self.kind in {WeatherKind.STORM, WeatherKind.SNOW, WeatherKind.WIND} and self.level >= 4

    def landing_add(self) -> int:
        return max(0, int(math.ceil(self.runway_slow * 5)))

    def gate_add(self) -> int:
        return max(0, int(math.ceil(self.gate_slow * 8)))

    def fuel_add(self) -> float:
        return max(0.0, self.fuel_slow)


@dataclass
class SimEvent:
    id: str
    sim_id: str
    tick: int
    kind: EventKind
    text: str
    data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def make(cls, sim_id: str, tick: int, kind: EventKind, text: str, data: dict[str, Any] | None = None) -> SimEvent:
        return cls(id=str(uuid4()), sim_id=sim_id, tick=tick, kind=kind, text=text, data=data or {})

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["kind"] = self.kind.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SimEvent:
        x = dict(data)
        x["kind"] = EventKind(x.get("kind", EventKind.ERROR.value))
        return cls(**x)


@dataclass
class SimMetrics:
    total_flights: int = 0
    completed: int = 0
    diverted: int = 0
    cancelled: int = 0
    active: int = 0
    waiting: int = 0
    emergencies: int = 0
    low_fuel_events: int = 0
    critical_fuel_events: int = 0
    average_delay: float = 0.0
    max_delay: int = 0
    min_delay: int = 0
    passenger_delay: int = 0
    throughput: float = 0.0
    runway_utilization: float = 0.0
    gate_utilization: float = 0.0
    fairness: float = 0.0
    airline_fairness: float = 0.0
    fuel_score: float = 0.0
    delay_score: float = 0.0
    safety_score: float = 0.0
    resource_score: float = 0.0
    overall_score: float = 0.0
    ticks: int = 0
    landed: int = 0
    average_wait: float = 0.0
    max_wait: int = 0
    events: int = 0
    weather_changes: int = 0
    runway_closures: int = 0
    gate_uses: int = 0
    total_fuel_left: float = 0.0
    average_fuel_left: float = 0.0
    airline_delays: dict[str, float] = field(default_factory=dict)
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SimMetrics:
        return cls(**data)

    def rounded(self) -> SimMetrics:
        data = self.to_dict()
        for key, val in list(data.items()):
            if isinstance(val, float):
                data[key] = round(val, 4)
        return SimMetrics.from_dict(data)


@dataclass
class SimConfig:
    name: str = "Airport Test"
    seed: int = 42
    algorithm: Algorithm = Algorithm.WEIGHTED
    flight_count: int = 30
    runway_count: int = 3
    gate_count: int = 12
    max_ticks: int = 1000
    tick_seconds: int = 60
    start_weather: WeatherKind = WeatherKind.CLEAR
    weather_on: bool = True
    failures_on: bool = True
    ai_on: bool = False
    random_arrivals: bool = True
    arrival_window: int = 80
    emergency_rate: float = 0.03
    failure_rate: float = 0.01
    weather_change_rate: float = 0.08
    low_fuel: float = 25.0
    critical_fuel: float = 12.0
    diversion_fuel: float = 6.0
    holding_fuel_cost: float = 0.7
    landing_fuel_cost: float = 2.0
    gate_hold_time: int = 18
    landing_time: int = 3
    runway_gap: int = 2
    passenger_weight: float = 0.02
    wait_weight: float = 1.1
    fuel_weight: float = 2.3
    emergency_weight: float = 100.0
    size_weight: float = 1.5
    fairness_weight: float = 1.0
    airport_code: str = "SIM"
    notes: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["algorithm"] = self.algorithm.value
        data["start_weather"] = self.start_weather.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SimConfig:
        x = dict(data)
        x["algorithm"] = Algorithm(x.get("algorithm", Algorithm.WEIGHTED.value))
        x["start_weather"] = WeatherKind(x.get("start_weather", WeatherKind.CLEAR.value))
        return cls(**x)

    def copy(self) -> SimConfig:
        return SimConfig.from_dict(self.to_dict())

    def check(self) -> list[str]:
        out = []
        if self.flight_count < 1:
            out.append("flight_count must be at least 1")
        if self.runway_count < 1:
            out.append("runway_count must be at least 1")
        if self.gate_count < 1:
            out.append("gate_count must be at least 1")
        if self.max_ticks < 10:
            out.append("max_ticks must be at least 10")
        if self.arrival_window < 0:
            out.append("arrival_window must be zero or more")
        if self.low_fuel <= self.critical_fuel:
            out.append("low_fuel must be above critical_fuel")
        if self.critical_fuel <= self.diversion_fuel:
            out.append("critical_fuel must be above diversion_fuel")
        if self.weather_change_rate < 0 or self.weather_change_rate > 1:
            out.append("weather_change_rate must be between 0 and 1")
        if self.emergency_rate < 0 or self.emergency_rate > 1:
            out.append("emergency_rate must be between 0 and 1")
        if self.failure_rate < 0 or self.failure_rate > 1:
            out.append("failure_rate must be between 0 and 1")
        return out


@dataclass
class SimState:
    id: str
    config: SimConfig
    tick: int = 0
    status: str = "created"
    flights: list[Flight] = field(default_factory=list)
    runways: list[Runway] = field(default_factory=list)
    gates: list[Gate] = field(default_factory=list)
    weather: Weather = field(default_factory=Weather)
    events: list[SimEvent] = field(default_factory=list)
    metrics: SimMetrics = field(default_factory=SimMetrics)
    created_at: str = ""
    updated_at: str = ""
    done_reason: str = ""
    ai_items: list[dict[str, Any]] = field(default_factory=list)
    values: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def make(cls, config: SimConfig) -> SimState:
        return cls(id=str(uuid4()), config=config)

    def to_dict(self, include_events: bool = True) -> dict[str, Any]:
        data = {
            "id": self.id,
            "config": self.config.to_dict(),
            "tick": self.tick,
            "status": self.status,
            "flights": [x.to_dict() for x in self.flights],
            "runways": [x.to_dict() for x in self.runways],
            "gates": [x.to_dict() for x in self.gates],
            "weather": self.weather.to_dict(),
            "metrics": self.metrics.to_dict(),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "done_reason": self.done_reason,
            "ai_items": copy.deepcopy(self.ai_items),
            "values": copy.deepcopy(self.values),
        }
        data["events"] = [x.to_dict() for x in self.events] if include_events else []
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SimState:
        return cls(
            id=data["id"],
            config=SimConfig.from_dict(data["config"]),
            tick=data.get("tick", 0),
            status=data.get("status", "created"),
            flights=[Flight.from_dict(x) for x in data.get("flights", [])],
            runways=[Runway.from_dict(x) for x in data.get("runways", [])],
            gates=[Gate.from_dict(x) for x in data.get("gates", [])],
            weather=Weather.from_dict(data.get("weather", {})),
            events=[SimEvent.from_dict(x) for x in data.get("events", [])],
            metrics=SimMetrics.from_dict(data.get("metrics", {})),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
            done_reason=data.get("done_reason", ""),
            ai_items=copy.deepcopy(data.get("ai_items", [])),
            values=copy.deepcopy(data.get("values", {})),
        )

    def copy(self) -> SimState:
        return SimState.from_dict(self.to_dict())

    def flight(self, flight_id: str) -> Flight | None:
        for item in self.flights:
            if item.id == flight_id:
                return item
        return None

    def runway(self, runway_id: str) -> Runway | None:
        for item in self.runways:
            if item.id == runway_id:
                return item
        return None

    def gate(self, gate_id: str) -> Gate | None:
        for item in self.gates:
            if item.id == gate_id:
                return item
        return None

    def waiting(self) -> list[Flight]:
        return [x for x in self.flights if x.is_waiting()]

    def active(self) -> list[Flight]:
        return [x for x in self.flights if not x.is_done()]

    def done(self) -> list[Flight]:
        return [x for x in self.flights if x.is_done()]

    def completed(self) -> list[Flight]:
        return [x for x in self.flights if x.status == FlightStatus.COMPLETED]

    def diverted(self) -> list[Flight]:
        return [x for x in self.flights if x.status == FlightStatus.DIVERTED]

    def all_done(self) -> bool:
        return bool(self.flights) and all(x.is_done() for x in self.flights)

    def open_runways(self) -> list[Runway]:
        return [x for x in self.runways if x.is_open()]

    def open_gates(self) -> list[Gate]:
        return [x for x in self.gates if x.is_open()]

    def event_count(self, kind: EventKind) -> int:
        return sum(1 for x in self.events if x.kind == kind)

    def json(self, include_events: bool = True) -> str:
        return json.dumps(self.to_dict(include_events=include_events), separators=(",", ":"))

    @classmethod
    def from_json(cls, text: str) -> SimState:
        return cls.from_dict(json.loads(text))


@dataclass
class ExperimentRun:
    algorithm: Algorithm
    run_number: int
    seed: int
    sim_id: str
    metrics: SimMetrics
    status: str = "done"
    error: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "algorithm": self.algorithm.value,
            "run_number": self.run_number,
            "seed": self.seed,
            "sim_id": self.sim_id,
            "metrics": self.metrics.to_dict(),
            "status": self.status,
            "error": self.error,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ExperimentRun:
        return cls(
            algorithm=Algorithm(data["algorithm"]),
            run_number=data["run_number"],
            seed=data["seed"],
            sim_id=data["sim_id"],
            metrics=SimMetrics.from_dict(data["metrics"]),
            status=data.get("status", "done"),
            error=data.get("error", ""),
        )


@dataclass
class Experiment:
    id: str
    name: str
    algorithms: list[Algorithm]
    runs: int
    base_config: SimConfig
    status: str = "created"
    items: list[ExperimentRun] = field(default_factory=list)
    summary: dict[str, Any] = field(default_factory=dict)
    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def make(cls, name: str, algorithms: list[Algorithm], runs: int, base_config: SimConfig) -> Experiment:
        return cls(id=str(uuid4()), name=name, algorithms=algorithms, runs=runs, base_config=base_config)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "algorithms": [x.value for x in self.algorithms],
            "runs": self.runs,
            "base_config": self.base_config.to_dict(),
            "status": self.status,
            "items": [x.to_dict() for x in self.items],
            "summary": copy.deepcopy(self.summary),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Experiment:
        return cls(
            id=data["id"],
            name=data["name"],
            algorithms=[Algorithm(x) for x in data.get("algorithms", [])],
            runs=data.get("runs", 1),
            base_config=SimConfig.from_dict(data["base_config"]),
            status=data.get("status", "created"),
            items=[ExperimentRun.from_dict(x) for x in data.get("items", [])],
            summary=copy.deepcopy(data.get("summary", {})),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
        )

    def copy(self) -> Experiment:
        return Experiment.from_dict(self.to_dict())


AIRCRAFT = {
    "C172": AircraftInfo(code="C172", name="Cessna 172", category="small", min_runway=800, seats=4, fuel_burn=0.25, landing_size=1, gate_time=8),
    "C208": AircraftInfo(code="C208", name="Cessna 208", category="small", min_runway=900, seats=12, fuel_burn=0.35, landing_size=1, gate_time=10),
    "E135": AircraftInfo(code="E135", name="Embraer 135", category="small", min_runway=1500, seats=37, fuel_burn=0.5, landing_size=1, gate_time=12),
    "E145": AircraftInfo(code="E145", name="Embraer 145", category="small", min_runway=1800, seats=50, fuel_burn=0.55, landing_size=1, gate_time=13),
    "CRJ2": AircraftInfo(code="CRJ2", name="CRJ 200", category="small", min_runway=1900, seats=50, fuel_burn=0.6, landing_size=1, gate_time=14),
    "CRJ7": AircraftInfo(code="CRJ7", name="CRJ 700", category="medium", min_runway=2100, seats=78, fuel_burn=0.7, landing_size=2, gate_time=15),
    "CRJ9": AircraftInfo(code="CRJ9", name="CRJ 900", category="medium", min_runway=2200, seats=90, fuel_burn=0.75, landing_size=2, gate_time=16),
    "E170": AircraftInfo(code="E170", name="Embraer 170", category="medium", min_runway=2100, seats=80, fuel_burn=0.72, landing_size=2, gate_time=15),
    "E175": AircraftInfo(code="E175", name="Embraer 175", category="medium", min_runway=2200, seats=88, fuel_burn=0.75, landing_size=2, gate_time=16),
    "E190": AircraftInfo(code="E190", name="Embraer 190", category="medium", min_runway=2300, seats=100, fuel_burn=0.8, landing_size=2, gate_time=17),
    "A220": AircraftInfo(code="A220", name="Airbus A220", category="medium", min_runway=2400, seats=140, fuel_burn=0.86, landing_size=2, gate_time=18),
    "B717": AircraftInfo(code="B717", name="Boeing 717", category="medium", min_runway=2300, seats=117, fuel_burn=0.82, landing_size=2, gate_time=18),
    "B737": AircraftInfo(code="B737", name="Boeing 737", category="medium", min_runway=2500, seats=180, fuel_burn=0.95, landing_size=2, gate_time=20),
    "B738": AircraftInfo(code="B738", name="Boeing 737-800", category="medium", min_runway=2600, seats=189, fuel_burn=1.0, landing_size=2, gate_time=21),
    "B739": AircraftInfo(code="B739", name="Boeing 737-900", category="medium", min_runway=2800, seats=220, fuel_burn=1.05, landing_size=2, gate_time=22),
    "B38M": AircraftInfo(code="B38M", name="Boeing 737 MAX 8", category="medium", min_runway=2600, seats=210, fuel_burn=0.98, landing_size=2, gate_time=21),
    "A318": AircraftInfo(code="A318", name="Airbus A318", category="medium", min_runway=2200, seats=132, fuel_burn=0.85, landing_size=2, gate_time=18),
    "A319": AircraftInfo(code="A319", name="Airbus A319", category="medium", min_runway=2300, seats=156, fuel_burn=0.9, landing_size=2, gate_time=19),
    "A320": AircraftInfo(code="A320", name="Airbus A320", category="medium", min_runway=2500, seats=186, fuel_burn=0.95, landing_size=2, gate_time=20),
    "A321": AircraftInfo(code="A321", name="Airbus A321", category="medium", min_runway=2800, seats=236, fuel_burn=1.08, landing_size=2, gate_time=23),
    "B752": AircraftInfo(code="B752", name="Boeing 757-200", category="large", min_runway=2900, seats=239, fuel_burn=1.2, landing_size=3, gate_time=24),
    "B753": AircraftInfo(code="B753", name="Boeing 757-300", category="large", min_runway=3000, seats=295, fuel_burn=1.28, landing_size=3, gate_time=25),
    "B763": AircraftInfo(code="B763", name="Boeing 767-300", category="large", min_runway=3000, seats=350, fuel_burn=1.4, landing_size=3, gate_time=27),
    "B764": AircraftInfo(code="B764", name="Boeing 767-400", category="large", min_runway=3100, seats=375, fuel_burn=1.48, landing_size=3, gate_time=28),
    "A300": AircraftInfo(code="A300", name="Airbus A300", category="large", min_runway=3000, seats=361, fuel_burn=1.45, landing_size=3, gate_time=28),
    "A310": AircraftInfo(code="A310", name="Airbus A310", category="large", min_runway=2800, seats=280, fuel_burn=1.35, landing_size=3, gate_time=26),
    "A332": AircraftInfo(code="A332", name="Airbus A330-200", category="large", min_runway=3100, seats=406, fuel_burn=1.55, landing_size=3, gate_time=30),
    "A333": AircraftInfo(code="A333", name="Airbus A330-300", category="large", min_runway=3200, seats=440, fuel_burn=1.62, landing_size=3, gate_time=31),
    "A339": AircraftInfo(code="A339", name="Airbus A330-900", category="large", min_runway=3200, seats=460, fuel_burn=1.58, landing_size=3, gate_time=31),
    "B772": AircraftInfo(code="B772", name="Boeing 777-200", category="heavy", min_runway=3300, seats=440, fuel_burn=1.75, landing_size=4, gate_time=34),
    "B773": AircraftInfo(code="B773", name="Boeing 777-300", category="heavy", min_runway=3400, seats=550, fuel_burn=1.9, landing_size=4, gate_time=36),
    "B77W": AircraftInfo(code="B77W", name="Boeing 777-300ER", category="heavy", min_runway=3500, seats=550, fuel_burn=1.95, landing_size=4, gate_time=37),
    "B788": AircraftInfo(code="B788", name="Boeing 787-8", category="heavy", min_runway=3200, seats=360, fuel_burn=1.65, landing_size=4, gate_time=32),
    "B789": AircraftInfo(code="B789", name="Boeing 787-9", category="heavy", min_runway=3300, seats=420, fuel_burn=1.72, landing_size=4, gate_time=34),
    "B78X": AircraftInfo(code="B78X", name="Boeing 787-10", category="heavy", min_runway=3400, seats=440, fuel_burn=1.8, landing_size=4, gate_time=35),
    "A342": AircraftInfo(code="A342", name="Airbus A340-200", category="heavy", min_runway=3400, seats=375, fuel_burn=1.8, landing_size=4, gate_time=35),
    "A343": AircraftInfo(code="A343", name="Airbus A340-300", category="heavy", min_runway=3500, seats=440, fuel_burn=1.9, landing_size=4, gate_time=36),
    "A346": AircraftInfo(code="A346", name="Airbus A340-600", category="heavy", min_runway=3700, seats=475, fuel_burn=2.05, landing_size=4, gate_time=39),
    "A359": AircraftInfo(code="A359", name="Airbus A350-900", category="heavy", min_runway=3400, seats=440, fuel_burn=1.72, landing_size=4, gate_time=34),
    "A35K": AircraftInfo(code="A35K", name="Airbus A350-1000", category="heavy", min_runway=3600, seats=480, fuel_burn=1.88, landing_size=4, gate_time=37),
    "B744": AircraftInfo(code="B744", name="Boeing 747-400", category="heavy", min_runway=3800, seats=660, fuel_burn=2.3, landing_size=5, gate_time=43),
    "B748": AircraftInfo(code="B748", name="Boeing 747-8", category="heavy", min_runway=3900, seats=605, fuel_burn=2.35, landing_size=5, gate_time=44),
    "A388": AircraftInfo(code="A388", name="Airbus A380", category="super", min_runway=4000, seats=853, fuel_burn=2.7, landing_size=6, gate_time=50),
    "MD80": AircraftInfo(code="MD80", name="McDonnell Douglas MD-80", category="medium", min_runway=2400, seats=172, fuel_burn=1.05, landing_size=2, gate_time=21),
    "MD11": AircraftInfo(code="MD11", name="McDonnell Douglas MD-11", category="heavy", min_runway=3400, seats=410, fuel_burn=1.95, landing_size=4, gate_time=37),
    "DC10": AircraftInfo(code="DC10", name="Douglas DC-10", category="heavy", min_runway=3400, seats=380, fuel_burn=2.0, landing_size=4, gate_time=38),
    "F100": AircraftInfo(code="F100", name="Fokker 100", category="medium", min_runway=2200, seats=109, fuel_burn=0.82, landing_size=2, gate_time=17),
    "AT72": AircraftInfo(code="AT72", name="ATR 72", category="small", min_runway=1400, seats=78, fuel_burn=0.45, landing_size=1, gate_time=13),
    "DH8D": AircraftInfo(code="DH8D", name="Dash 8 Q400", category="small", min_runway=1500, seats=90, fuel_burn=0.48, landing_size=1, gate_time=14),
    "GLF6": AircraftInfo(code="GLF6", name="Gulfstream G650", category="small", min_runway=1800, seats=19, fuel_burn=0.6, landing_size=1, gate_time=11),
}

AIRCRAFT_CODES = list(AIRCRAFT.keys())

def get_aircraft(code: str) -> AircraftInfo:
    return AIRCRAFT.get(code, AIRCRAFT["A320"])

def aircraft_by_category(category: str) -> list[AircraftInfo]:
    return [x for x in AIRCRAFT.values() if x.category == category]

def aircraft_for_runway(length: int) -> list[AircraftInfo]:
    return [x for x in AIRCRAFT.values() if x.min_runway <= length]

def all_categories() -> list[str]:
    return sorted({x.category for x in AIRCRAFT.values()})

def make_id() -> str:
    return str(uuid4())

def clean_number(val: Any, default: float = 0.0) -> float:
    try:
        out = float(val)
        if math.isnan(out) or math.isinf(out):
            return default
        return out
    except (TypeError, ValueError):
        return default

def clean_int(val: Any, default: int = 0) -> int:
    try:
        return int(val)
    except (TypeError, ValueError):
        return default

def clamp(val: float, low: float, high: float) -> float:
    return max(low, min(high, val))

def average(vals: list[float]) -> float:
    if not vals:
        return 0.0
    return sum(vals) / len(vals)

def safe_json(data: Any) -> str:
    return json.dumps(data, default=str, separators=(",", ":"))

def safe_copy(data: Any) -> Any:
    return copy.deepcopy(data)
