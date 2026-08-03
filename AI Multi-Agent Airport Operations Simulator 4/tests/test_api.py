from fastapi.testclient import TestClient
from app.main import app

a = TestClient(app)

def test_a():
    b = a.get("/health")
    assert b.status_code == 200
    assert b.json()["ok"] is True

def test_b():
    b = a.post("/simulations", json={"a": 42, "b": 20, "c": "weighted", "d": "x"})
    assert b.status_code == 200
    c = b.json()["id"]
    d = a.post(f"/simulations/{c}/step", json={"a": 10})
    assert d.status_code == 200
    assert d.json()["state"]["time"] == 10

def test_c():
    b = a.post("/experiments/run", json={"a": 2, "b": 20, "c": 10})
    assert b.status_code == 200
    assert "fcfs" in b.json()
