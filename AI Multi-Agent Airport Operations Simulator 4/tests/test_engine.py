from app.sim.scenarios import a
from app.sim.engine import X
from app.domain.enums import C, A
from app.sim.schedulers import d, i

def test_a():
    b, c, d1, e = a(42, 30)
    f = X("x", b, c, d1, e, C.c, 42)
    g = f.r(120)
    assert f.i == 120
    assert len(g) > 0

def test_b():
    b, c, d1, e = a(2, 10)
    b[0].g = True
    assert i(b, 0, C.c).a == b[0].a

def test_c():
    b, c, d1, e = a(3, 20)
    f = X("x", b, c, d1, e, C.a, 3)
    f.r(200)
    for g in c:
        assert g.f >= 0

def test_d():
    b, c, d1, e = a(4, 20)
    f = X("x", b, c, d1, e, C.b, 4)
    f.r(200)
    assert all(g.b <= 80 for g in b)

def test_e():
    b, c, d1, e = a(5, 20)
    f = X("x", b, c, d1, e, C.d, 5)
    x = f.s()
    assert x["id"] == "x"
    assert "metrics" in x
