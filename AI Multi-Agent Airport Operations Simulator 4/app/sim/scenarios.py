import random
from app.domain.models import C, D, E, F
from app.domain.enums import A, B

def a(b: int, c: int = 30):
    d = random.Random(b)
    e = [
        D("R1", 3600),
        D("R2", 3000)
    ]
    f = []
    for g in range(1, 9):
        f.append(E(f"G{g}", "big" if g <= 3 else "mid"))
    h = []
    for g in range(c):
        i = d.randint(20, 80)
        j = d.randint(50, 330)
        k = d.randint(0, 90)
        l = d.choice([2200, 2500, 2800, 3200])
        m = ["big", "mid"] if j > 200 else ["mid", "big"]
        h.append(C(f"F{b:03d}{g:03d}", i, j, k, l, m))
    return h, e, f, F(B.a, 10.0, 5.0, set(), 1.0)
