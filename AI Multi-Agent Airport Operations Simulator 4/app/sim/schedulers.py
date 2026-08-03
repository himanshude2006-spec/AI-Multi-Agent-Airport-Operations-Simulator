from app.domain.models import C, D
from app.domain.enums import C as Z

def a(b: C, c: int):
    return max(0, c - b.d)

def d(b: C, c: int):
    e = 100000 if b.g else 0
    f = max(0, 60 - b.b) * 20
    g = b.c * 0.5
    h = a(b, c) * 10
    return e + f + g + h

def i(b: list[C], c: int, d2: Z):
    if not b:
        return None
    if d2 == Z.a:
        return min(b, key=lambda e: (e.d, e.a))
    if d2 == Z.b:
        return min(b, key=lambda e: (e.b, e.d))
    if d2 == Z.c:
        return max(b, key=lambda e: d(e, c))
    return j(b, c)

def j(b: list[C], c: int):
    try:
        from ortools.sat.python import cp_model
        d2 = cp_model.CpModel()
        e = []
        for x, y in enumerate(b):
            z = d2.new_bool_var(f"x{x}")
            e.append(z)
        d2.add(sum(e) == 1)
        q = []
        for x, y in enumerate(b):
            q.append(int(d(y, c)) * e[x])
        d2.maximize(sum(q))
        r = cp_model.CpSolver()
        s = r.solve(d2)
        if s in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            for x, y in enumerate(e):
                if r.value(y):
                    return b[x]
    except Exception:
        pass
    return max(b, key=lambda e: d(e, c))

def k(b: C, c: list[D], d2: int):
    e = [x for x in c if not x.d and x.c <= d2 and x.b >= b.e]
    if not e:
        return None
    return min(e, key=lambda x: (x.c, -x.b, x.a))
