from enum import StrEnum

class A(StrEnum):
    a = "approaching"
    b = "holding"
    c = "cleared"
    d = "landing"
    e = "landed"
    f = "taxiing"
    g = "at_gate"
    h = "departed"
    i = "diverted"

class B(StrEnum):
    a = "clear"
    b = "rain"
    c = "fog"
    d = "storm"
    e = "snow"
    f = "wind"

class C(StrEnum):
    a = "fcfs"
    b = "fuel"
    c = "weighted"
    d = "solver"

class D(StrEnum):
    a = "flight_created"
    b = "landing_requested"
    c = "fuel_low"
    d = "fuel_critical"
    e = "runway_assigned"
    f = "landing_started"
    g = "landing_done"
    h = "gate_assigned"
    i = "gate_reached"
    j = "weather_changed"
    k = "runway_closed"
    l = "runway_opened"
    m = "diverted"
    n = "tick"
    o = "decision"
