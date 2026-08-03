from dataclasses import asdict
from app.sim.scenarios import a
from app.sim.engine import X
from app.domain.enums import C
from app.sim.metrics import a as mm

def b(c: int, d: int, e: int):
    f = {}
    for g in list(C):
        h = []
        for i in range(c):
            j = i + 1000
            k, l, m, n = a(j, e)
            o = X(f"{g}-{j}", k, l, m, n, g, j)
            o.r(d)
            h.append(asdict(mm(o.b, o.c, o.d, o.i)))
        f[g] = {
            "runs": c,
            "avg_delay": sum(x["a"] for x in h) / c,
            "avg_diversions": sum(x["b"] for x in h) / c,
            "avg_emergencies": sum(x["c"] for x in h) / c,
            "avg_runway_use": sum(x["d"] for x in h) / c,
            "avg_gate_use": sum(x["e"] for x in h) / c,
            "avg_done": sum(x["f"] for x in h) / c,
            "avg_passenger_delay": sum(x["g"] for x in h) / c,
            "avg_score": sum(x["h"] for x in h) / c
        }
    return f
