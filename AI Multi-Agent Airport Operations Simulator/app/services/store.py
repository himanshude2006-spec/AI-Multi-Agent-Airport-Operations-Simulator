import uuid
from app.sim.engine import X
from app.sim.scenarios import a
from app.domain.enums import C

class A:
    def __init__(self):
        self.a = {}

    def b(self, c: int, d: int, e: C):
        f = str(uuid.uuid4())
        g, h, i, j = a(c, d)
        k = X(f, g, h, i, j, e, c)
        self.a[f] = k
        return k

    def c(self, d: str):
        return self.a.get(d)

e = A()
