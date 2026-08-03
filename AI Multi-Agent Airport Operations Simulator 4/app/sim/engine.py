import random
from dataclasses import asdict
from app.domain.models import C, D, E, F, G
from app.domain.enums import A, B, C as Z, D as Y
from app.sim.schedulers import i, k
from app.sim.metrics import a as mm

class X:
    def __init__(self, a: str, b: list[C], c: list[D], d: list[E], e: F, f: Z, g: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = random.Random(g)
        self.i = 0
        self.j = []
        self.k = True

    def l(self, a: str, b: str, c: dict):
        d = G(a, self.i, b, c)
        self.j.append(d)
        return d

    def m(self):
        a = []
        for b in self.b:
            if b.h in {A.a, A.b, A.c}:
                b.b -= 1
                if b.b <= 12 and not b.g:
                    b.g = True
                    a.append(self.l(Y.d, f"flight:{b.a}", {"id": b.a, "fuel": b.b}))
                elif b.b <= 25:
                    a.append(self.l(Y.c, f"flight:{b.a}", {"id": b.a, "fuel": b.b}))
                if b.b <= 0 and b.h not in {A.e, A.f, A.g, A.h}:
                    b.h = A.i
                    b.m = self.i
                    a.append(self.l(Y.m, f"flight:{b.a}", {"id": b.a}))
        return a

    def n(self):
        a = []
        if self.h.random() < 0.04:
            b = self.h.choice(list(B))
            self.e.a = b
            if b == B.c:
                self.e.b = 1.5
                self.e.e = 1.5
            elif b == B.d:
                self.e.b = 2.5
                self.e.e = 2.0
            elif b == B.f:
                self.e.c = 35.0
                self.e.e = 1.4
            else:
                self.e.b = 10.0
                self.e.c = 5.0
                self.e.e = 1.0
            a.append(self.l(Y.j, "weather", {"kind": b, "visibility": self.e.b, "wind": self.e.c}))
        if self.h.random() < 0.015:
            b = self.h.choice(self.c)
            b.d = True
            b.e = self.i
            a.append(self.l(Y.k, f"runway:{b.a}", {"id": b.a}))
        for b in self.c:
            if b.d and self.i - b.e >= 12:
                b.d = False
                a.append(self.l(Y.l, f"runway:{b.a}", {"id": b.a}))
        return a

    def o(self):
        a = []
        b = [x for x in self.b if x.h in {A.a, A.b} and x.d <= self.i]
        c = [x for x in self.c if not x.d and x.c <= self.i]
        for d in c:
            e = i(b, self.i, self.f)
            if not e:
                break
            if d.b < e.e:
                b.remove(e)
                continue
            e.h = A.d
            e.i = d.a
            e.k = self.i
            d.c = self.i + int(4 * self.e.e)
            d.f += int(4 * self.e.e)
            a.append(self.l(Y.e, "scheduler", {"flight": e.a, "runway": d.a, "mode": self.f}))
            b.remove(e)
        return a

    def p(self):
        a = []
        for b in self.b:
            if b.h == A.d and b.i:
                c = next(x for x in self.c if x.a == b.i)
                if self.i >= c.c:
                    b.h = A.e
                    b.l = self.i
                    a.append(self.l(Y.g, f"flight:{b.a}", {"id": b.a, "runway": b.i}))
            if b.h == A.e:
                c = k(b, self.d, self.i)
                if c:
                    b.j = c.a
                    b.h = A.f
                    c.c = self.i + 3
                    c.e += 3
                    a.append(self.l(Y.h, "gate", {"flight": b.a, "gate": c.a}))
            if b.h == A.f and b.j:
                c = next(x for x in self.d if x.a == b.j)
                if self.i >= c.c:
                    b.h = A.g
                    c.c = self.i + 25
                    c.e += 25
                    a.append(self.l(Y.i, f"flight:{b.a}", {"id": b.a, "gate": c.a}))
        return a

    def q(self):
        a = []
        a += self.m()
        a += self.n()
        a += self.o()
        a += self.p()
        a.append(self.l(Y.n, "sim", {"time": self.i}))
        self.i += 1
        return a

    def r(self, a: int):
        b = []
        for _ in range(a):
            b.extend(self.q())
        return b

    def s(self):
        return {
            "id": self.a,
            "time": self.i,
            "mode": self.f,
            "weather": asdict(self.e),
            "flights": [asdict(x) for x in self.b],
            "runways": [asdict(x) for x in self.c],
            "gates": [asdict(x) for x in self.d],
            "metrics": asdict(mm(self.b, self.c, self.d, self.i))
        }
