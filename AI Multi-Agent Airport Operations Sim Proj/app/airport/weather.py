from __future__ import annotations

import random
from dataclasses import dataclass, asdict
from typing import Any

from app.other.types import Weather, WeatherKind, Runway, RunwayStatus, Gate


@dataclass
class WeatherRule:
    kind: WeatherKind
    min_level: int
    max_level: int
    wind_low: int
    wind_high: int
    visibility_low: int
    visibility_high: int
    temp_low: int
    temp_high: int
    runway_slow_base: float
    gate_slow_base: float
    fuel_slow_base: float
    runway_close_chance: float
    gate_close_chance: float
    next_items: list[WeatherKind]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["kind"] = self.kind.value
        data["next_items"] = [x.value for x in self.next_items]
        return data


RULES = {
    WeatherKind.CLEAR: WeatherRule(
        kind=WeatherKind.CLEAR,
        min_level=0,
        max_level=1,
        wind_low=1,
        wind_high=12,
        visibility_low=8,
        visibility_high=15,
        temp_low=10,
        temp_high=32,
        runway_slow_base=0.0,
        gate_slow_base=0.0,
        fuel_slow_base=0.0,
        runway_close_chance=0.0,
        gate_close_chance=0.0,
        next_items=[WeatherKind.CLEAR, WeatherKind.CLEAR, WeatherKind.RAIN, WeatherKind.FOG, WeatherKind.WIND],
    ),
    WeatherKind.RAIN: WeatherRule(
        kind=WeatherKind.RAIN,
        min_level=1,
        max_level=4,
        wind_low=5,
        wind_high=28,
        visibility_low=4,
        visibility_high=10,
        temp_low=8,
        temp_high=28,
        runway_slow_base=0.15,
        gate_slow_base=0.10,
        fuel_slow_base=0.08,
        runway_close_chance=0.02,
        gate_close_chance=0.01,
        next_items=[WeatherKind.CLEAR, WeatherKind.RAIN, WeatherKind.RAIN, WeatherKind.FOG, WeatherKind.STORM],
    ),
    WeatherKind.FOG: WeatherRule(
        kind=WeatherKind.FOG,
        min_level=1,
        max_level=5,
        wind_low=0,
        wind_high=10,
        visibility_low=1,
        visibility_high=5,
        temp_low=2,
        temp_high=18,
        runway_slow_base=0.35,
        gate_slow_base=0.08,
        fuel_slow_base=0.12,
        runway_close_chance=0.08,
        gate_close_chance=0.00,
        next_items=[WeatherKind.CLEAR, WeatherKind.FOG, WeatherKind.FOG, WeatherKind.RAIN],
    ),
    WeatherKind.STORM: WeatherRule(
        kind=WeatherKind.STORM,
        min_level=2,
        max_level=5,
        wind_low=20,
        wind_high=65,
        visibility_low=1,
        visibility_high=7,
        temp_low=5,
        temp_high=30,
        runway_slow_base=0.55,
        gate_slow_base=0.30,
        fuel_slow_base=0.25,
        runway_close_chance=0.30,
        gate_close_chance=0.12,
        next_items=[WeatherKind.RAIN, WeatherKind.STORM, WeatherKind.STORM, WeatherKind.WIND, WeatherKind.CLEAR],
    ),
    WeatherKind.SNOW: WeatherRule(
        kind=WeatherKind.SNOW,
        min_level=1,
        max_level=5,
        wind_low=5,
        wind_high=35,
        visibility_low=1,
        visibility_high=7,
        temp_low=-18,
        temp_high=3,
        runway_slow_base=0.45,
        gate_slow_base=0.35,
        fuel_slow_base=0.18,
        runway_close_chance=0.20,
        gate_close_chance=0.10,
        next_items=[WeatherKind.SNOW, WeatherKind.SNOW, WeatherKind.CLEAR, WeatherKind.WIND, WeatherKind.FOG],
    ),
    WeatherKind.WIND: WeatherRule(
        kind=WeatherKind.WIND,
        min_level=1,
        max_level=5,
        wind_low=20,
        wind_high=70,
        visibility_low=6,
        visibility_high=14,
        temp_low=3,
        temp_high=30,
        runway_slow_base=0.25,
        gate_slow_base=0.12,
        fuel_slow_base=0.15,
        runway_close_chance=0.12,
        gate_close_chance=0.03,
        next_items=[WeatherKind.CLEAR, WeatherKind.WIND, WeatherKind.WIND, WeatherKind.STORM, WeatherKind.RAIN],
    ),
}


class WeatherMaker:
    def __init__(self, seed: int = 42) -> None:
        self.random = random.Random(seed)
        self.seed = seed
        self.changes = 0
        self.last_roll = 0.0
        self.history: list[dict[str, Any]] = []

    def reset(self, seed: int | None = None) -> None:
        if seed is not None:
            self.seed = seed
        self.random = random.Random(self.seed)
        self.changes = 0
        self.last_roll = 0.0
        self.history.clear()

    def make(self, kind: WeatherKind, tick: int = 0, level: int | None = None) -> Weather:
        rule = RULES[kind]
        val = level if level is not None else self.random.randint(rule.min_level, rule.max_level)
        val = max(rule.min_level, min(rule.max_level, val))
        wind = self.random.randint(rule.wind_low, rule.wind_high)
        vis = self.random.randint(rule.visibility_low, rule.visibility_high)
        temp = self.random.randint(rule.temp_low, rule.temp_high)
        mult = max(0.2, val / max(1, rule.max_level))
        item = Weather(
            kind=kind,
            level=val,
            wind=wind,
            visibility=vis,
            temp=temp,
            changed_tick=tick,
            runway_slow=round(rule.runway_slow_base * mult, 3),
            gate_slow=round(rule.gate_slow_base * mult, 3),
            fuel_slow=round(rule.fuel_slow_base * mult, 3),
            close_count=0,
            notes=[],
        )
        item.notes = self.notes(item)
        self.history.append(item.to_dict())
        return item

    def maybe_change(self, old: Weather, tick: int, rate: float) -> Weather | None:
        self.last_roll = self.random.random()
        if self.last_roll >= rate:
            return None
        rule = RULES[old.kind]
        kind = self.random.choice(rule.next_items)
        if kind == old.kind:
            step = self.random.choice([-1, 0, 1])
            level = max(rule.min_level, min(rule.max_level, old.level + step))
        else:
            level = None
        item = self.make(kind, tick=tick, level=level)
        self.changes += 1
        return item

    def force(self, name: str, tick: int, level: int | None = None) -> Weather:
        return self.make(WeatherKind(name), tick=tick, level=level)

    def notes(self, item: Weather) -> list[str]:
        out = []
        if item.kind == WeatherKind.CLEAR:
            out.append("normal operations")
        if item.kind == WeatherKind.RAIN:
            out.append("wet runway")
        if item.kind == WeatherKind.FOG:
            out.append("low visibility")
        if item.kind == WeatherKind.STORM:
            out.append("storm cells near airport")
        if item.kind == WeatherKind.SNOW:
            out.append("snow removal may be needed")
        if item.kind == WeatherKind.WIND:
            out.append("crosswind checks required")
        if item.wind >= 40:
            out.append("high wind")
        if item.visibility <= 2:
            out.append("very low visibility")
        if item.temp <= 0:
            out.append("freezing conditions")
        if item.level >= 4:
            out.append("severe conditions")
        return out

    def runway_time(self, base: int, item: Weather) -> int:
        add = int(round(base * item.runway_slow))
        if item.visibility <= 2:
            add += 1
        if item.wind >= 45:
            add += 1
        return max(1, base + add)

    def gate_time(self, base: int, item: Weather) -> int:
        add = int(round(base * item.gate_slow))
        if item.kind == WeatherKind.SNOW:
            add += 2
        return max(1, base + add)

    def fuel_cost(self, base: float, item: Weather) -> float:
        return round(base + item.fuel_slow, 3)

    def close_roll(self, item: Weather) -> bool:
        rule = RULES[item.kind]
        chance = rule.runway_close_chance * max(1, item.level)
        chance = min(0.85, chance)
        return self.random.random() < chance

    def gate_close_roll(self, item: Weather) -> bool:
        rule = RULES[item.kind]
        chance = rule.gate_close_chance * max(1, item.level)
        chance = min(0.55, chance)
        return self.random.random() < chance

    def close_length(self, item: Weather) -> int:
        base = 2 + item.level * 2
        if item.kind == WeatherKind.SNOW:
            base += 4
        if item.kind == WeatherKind.STORM:
            base += 3
        return self.random.randint(max(2, base - 2), base + 4)

    def reopen_ok(self, item: Weather) -> bool:
        if item.kind == WeatherKind.CLEAR:
            return True
        if item.kind == WeatherKind.RAIN and item.level <= 2:
            return self.random.random() < 0.55
        if item.kind == WeatherKind.FOG and item.visibility >= 4:
            return self.random.random() < 0.40
        if item.kind == WeatherKind.WIND and item.wind < 35:
            return self.random.random() < 0.35
        return self.random.random() < 0.10

    def score(self, item: Weather) -> float:
        val = item.level * 15.0
        val += item.runway_slow * 30.0
        val += item.gate_slow * 20.0
        val += item.fuel_slow * 25.0
        if item.visibility <= 2:
            val += 15.0
        if item.wind >= 40:
            val += 20.0
        return round(min(100.0, val), 2)

    def summary(self, item: Weather) -> dict[str, Any]:
        return {
            "kind": item.kind.value,
            "level": item.level,
            "wind": item.wind,
            "visibility": item.visibility,
            "temp": item.temp,
            "risk": self.score(item),
            "notes": list(item.notes),
            "landing_add": item.landing_add(),
            "gate_add": item.gate_add(),
            "fuel_add": item.fuel_add(),
        }

    def runway_actions(self, item: Weather, runways: list[Runway], tick: int) -> list[dict[str, Any]]:
        out = []
        if item.is_dangerous():
            for runway in runways:
                if runway.status == RunwayStatus.OPEN and self.close_roll(item):
                    length = self.close_length(item)
                    out.append({"action": "close", "runway_id": runway.id, "until": tick + length, "reason": item.kind.value})
        else:
            for runway in runways:
                if runway.status == RunwayStatus.CLOSED and runway.failed_until <= tick and self.reopen_ok(item):
                    out.append({"action": "open", "runway_id": runway.id, "reason": item.kind.value})
        return out

    def gate_actions(self, item: Weather, gates: list[Gate], tick: int) -> list[dict[str, Any]]:
        out = []
        if item.kind in {WeatherKind.STORM, WeatherKind.SNOW} and item.level >= 3:
            for gate in gates:
                if gate.is_open() and self.gate_close_roll(item):
                    out.append({"action": "close", "gate_id": gate.id, "until": tick + self.close_length(item), "reason": item.kind.value})
        return out

    def forecast(self, item: Weather, count: int = 5) -> list[dict[str, Any]]:
        old_state = self.random.getstate()
        out = []
        cur = item.copy()
        for i in range(count):
            rule = RULES[cur.kind]
            kind = self.random.choice(rule.next_items)
            cur = self.make(kind, tick=cur.changed_tick + i + 1)
            out.append(self.summary(cur))
        self.random.setstate(old_state)
        return out

    def catalog(self) -> list[dict[str, Any]]:
        return [RULES[x].to_dict() for x in WeatherKind]


def weather_names() -> list[str]:
    return [x.value for x in WeatherKind]


def weather_rule(name: str) -> dict[str, Any]:
    return RULES[WeatherKind(name)].to_dict()


def weather_risk(item: Weather) -> str:
    maker = WeatherMaker(1)
    val = maker.score(item)
    if val >= 80:
        return "extreme"
    if val >= 60:
        return "high"
    if val >= 35:
        return "medium"
    if val >= 15:
        return "low"
    return "normal"


def weather_text(item: Weather) -> str:
    return f"{item.kind.value} level {item.level}, wind {item.wind}, visibility {item.visibility}, temperature {item.temp}"
