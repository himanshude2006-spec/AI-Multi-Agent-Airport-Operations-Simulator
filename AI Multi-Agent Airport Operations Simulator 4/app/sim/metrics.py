from app.domain.models import C, D, E, I

def a(b: list[C], c: list[D], d: list[E], e: int):
    f = I()
    g = [x for x in b if x.h.value in {"landed", "taxiing", "at_gate", "departed"}]
    h = [max(0, x.l - x.d) for x in g]
    f.a = sum(h) / len(h) if h else 0.0
    f.b = len([x for x in b if x.h.value == "diverted"])
    f.c = len([x for x in b if x.g])
    f.d = sum(x.f for x in c) / (max(1, e) * len(c)) if c else 0.0
    f.e = sum(x.e for x in d) / (max(1, e) * len(d)) if d else 0.0
    f.f = len(g)
    f.g = sum(max(0, x.l - x.d) * x.c for x in g)
    f.h = f.a + f.b * 100 + f.c * 1000 + f.g * 0.01
    return f
