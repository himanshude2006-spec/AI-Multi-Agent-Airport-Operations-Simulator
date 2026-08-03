import os

from fastapi.testclient import TestClient

from app.main import app
from app.settings import settings


settings.use_redis = False
settings.use_celery = False
settings.use_ai = False
settings.use_database = True


def body(**data):
    vals = {
        "name": "API Test",
        "seed": 10,
        "algorithm": "weighted",
        "flight_count": 5,
        "runway_count": 2,
        "gate_count": 4,
        "max_ticks": 150,
        "arrival_window": 5,
        "weather_on": False,
        "failures_on": False,
        "emergency_rate": 0,
        "failure_rate": 0,
        "weather_change_rate": 0,
    }
    vals.update(data)
    return vals


def create(client, **data):
    res = client.post("/api/simulations", json=body(**data))
    assert res.status_code == 200
    return res.json()


def test_root():
    with TestClient(app) as client:
        res = client.get("/")
        assert res.status_code == 200
        data = res.json()
        assert data["name"] == "AI Multi-Agent Airport Operations Simulator"
        assert data["backend_only"] is True


def test_top_health():
    with TestClient(app) as client:
        res = client.get("/health")
        assert res.status_code == 200
        assert res.json()["ok"] is True


def test_api_health():
    with TestClient(app) as client:
        res = client.get("/api/health")
        assert res.status_code == 200
        assert res.json()["ok"] is True


def test_about():
    with TestClient(app) as client:
        res = client.get("/about")
        assert res.status_code == 200
        data = res.json()
        assert data["frontend"] is False
        assert "simulation engine" in data["components"]


def test_runtime():
    with TestClient(app) as client:
        res = client.get("/runtime")
        assert res.status_code == 200
        assert "engines" in res.json()


def test_settings():
    with TestClient(app) as client:
        res = client.get("/api/settings")
        assert res.status_code == 200
        data = res.json()
        assert data["app_name"] == "AI Multi-Agent Airport Operations Simulator"
        assert data["openai_api_key"] in {"", "set"}


def test_catalog():
    with TestClient(app) as client:
        res = client.get("/api/catalog")
        assert res.status_code == 200
        data = res.json()
        assert "weighted" in data["algorithms"]
        assert "storm" in data["weather"]


def test_weather_catalog_item():
    with TestClient(app) as client:
        res = client.get("/api/weather/storm")
        assert res.status_code == 200
        assert res.json()["kind"] == "storm"


def test_weather_catalog_bad():
    with TestClient(app) as client:
        res = client.get("/api/weather/not-real")
        assert res.status_code == 404


def test_create_simulation():
    with TestClient(app) as client:
        data = create(client)
        assert data["config"]["name"] == "API Test"
        assert len(data["flights"]) == 5
        assert len(data["runways"]) == 2
        assert len(data["gates"]) == 4


def test_list_simulations():
    with TestClient(app) as client:
        create(client)
        res = client.get("/api/simulations")
        assert res.status_code == 200
        assert res.json()["count"] >= 1


def test_get_simulation():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}")
        assert res.status_code == 200
        assert res.json()["id"] == data["id"]


def test_get_missing_simulation():
    with TestClient(app) as client:
        res = client.get("/api/simulations/missing")
        assert res.status_code == 404


def test_start_simulation():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/start")
        assert res.status_code == 200
        assert res.json()["status"] == "running"


def test_pause_simulation():
    with TestClient(app) as client:
        data = create(client)
        client.post(f"/api/simulations/{data['id']}/start")
        res = client.post(f"/api/simulations/{data['id']}/pause")
        assert res.status_code == 200
        assert res.json()["status"] == "paused"


def test_tick_simulation():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/tick", json={"ticks": 3})
        assert res.status_code == 200
        assert res.json()["tick"] == 3


def test_run_simulation():
    with TestClient(app) as client:
        data = create(client, flight_count=2, arrival_window=1)
        res = client.post(f"/api/simulations/{data['id']}/run", json={"max_ticks": 10, "background": False})
        assert res.status_code == 200
        assert res.json()["tick"] <= 10


def test_run_until():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/run-until/4")
        assert res.status_code == 200
        assert res.json()["tick"] == 4


def test_metrics():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/metrics")
        assert res.status_code == 200
        assert "metrics" in res.json()


def test_metric_summary():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/metrics/summary")
        assert res.status_code == 200
        assert "fuel" in res.json()
        assert "delay" in res.json()


def test_events():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/events")
        assert res.status_code == 200
        assert res.json()["count"] >= 1


def test_flights():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/flights")
        assert res.status_code == 200
        assert res.json()["count"] == 5


def test_flight_detail():
    with TestClient(app) as client:
        data = create(client)
        flight_id = data["flights"][0]["id"]
        res = client.get(f"/api/simulations/{data['id']}/flights/{flight_id}")
        assert res.status_code == 200
        assert res.json()["flight"]["id"] == flight_id


def test_add_flight():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/flights", json={"airline": "ZZ", "number": "77", "aircraft": "A320", "fuel": 60, "arrival_tick": 0})
        assert res.status_code == 200
        assert res.json()["airline"] == "ZZ"


def test_emergency_flight():
    with TestClient(app) as client:
        data = create(client)
        flight_id = data["flights"][0]["id"]
        res = client.post(f"/api/simulations/{data['id']}/flights/{flight_id}/emergency", json={"reason": "test"})
        assert res.status_code == 200
        assert res.json()["emergency"] is True


def test_divert_flight():
    with TestClient(app) as client:
        data = create(client)
        flight_id = data["flights"][0]["id"]
        res = client.post(f"/api/simulations/{data['id']}/flights/{flight_id}/divert", json={"reason": "test"})
        assert res.status_code == 200
        assert res.json()["status"] == "diverted"


def test_runways():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/runways")
        assert res.status_code == 200
        assert res.json()["count"] == 2


def test_add_runway():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/runways", json={"name": "RNEW", "length": 4000})
        assert res.status_code == 200
        assert res.json()["name"] == "RNEW"


def test_close_open_runway():
    with TestClient(app) as client:
        data = create(client)
        runway_id = data["runways"][0]["id"]
        res = client.post(f"/api/simulations/{data['id']}/runways/{runway_id}/close", json={"ticks": 4, "reason": "test"})
        assert res.status_code == 200
        assert res.json()["status"] == "closed"
        res = client.post(f"/api/simulations/{data['id']}/runways/{runway_id}/open")
        assert res.status_code == 200
        assert res.json()["status"] == "open"


def test_gates():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/gates")
        assert res.status_code == 200
        assert res.json()["count"] == 4


def test_add_gate():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/gates", json={"name": "GNEW", "categories": ["medium", "large"]})
        assert res.status_code == 200
        assert res.json()["name"] == "GNEW"


def test_force_weather():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/weather", json={"kind": "fog", "level": 3})
        assert res.status_code == 200
        assert res.json()["kind"] == "fog"
        assert res.json()["level"] == 3


def test_scheduler_info():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/scheduler")
        assert res.status_code == 200
        assert res.json()["current"] == "weighted"


def test_scheduler_rank():
    with TestClient(app) as client:
        data = create(client, arrival_window=0)
        client.post(f"/api/simulations/{data['id']}/tick", json={"ticks": 1})
        res = client.get(f"/api/simulations/{data['id']}/scheduler/rank?algorithm=fuel")
        assert res.status_code == 200
        assert res.json()["algorithm"] == "fuel"


def test_scheduler_compare():
    with TestClient(app) as client:
        data = create(client, arrival_window=0)
        client.post(f"/api/simulations/{data['id']}/tick", json={"ticks": 1})
        res = client.get(f"/api/simulations/{data['id']}/scheduler/compare")
        assert res.status_code == 200
        assert "fcfs" in res.json()


def test_ai_local():
    with TestClient(app) as client:
        data = create(client, arrival_window=0)
        client.post(f"/api/simulations/{data['id']}/tick", json={"ticks": 1})
        res = client.post(f"/api/simulations/{data['id']}/ai", json={"use_ai": False})
        assert res.status_code == 200
        assert res.json()["count"] >= 1


def test_ai_apply_no_action():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/ai/apply", json={"action": "no_action", "target": "", "reason": "stable", "confidence": 0.5})
        assert res.status_code == 200
        assert res.json()["applied"] is True


def test_ai_history():
    with TestClient(app) as client:
        data = create(client)
        client.post(f"/api/simulations/{data['id']}/ai", json={"use_ai": False})
        res = client.get(f"/api/simulations/{data['id']}/ai")
        assert res.status_code == 200
        assert res.json()["count"] >= 1


def test_check_sim():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/check")
        assert res.status_code == 200
        assert res.json()["ok"] is True


def test_repair_sim():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/repair")
        assert res.status_code == 200
        assert "fixed" in res.json()


def test_snapshots():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/snapshots")
        assert res.status_code == 200
        assert res.json()["count"] == 0


def test_experiment():
    with TestClient(app) as client:
        data = {
            "name": "API Experiment",
            "algorithms": ["fcfs", "fuel"],
            "runs": 1,
            "config": body(flight_count=2, runway_count=1, gate_count=2, arrival_window=1, max_ticks=100),
            "background": False,
        }
        res = client.post("/api/experiments", json=data)
        assert res.status_code == 200
        out = res.json()
        assert out["status"] == "completed"
        assert len(out["items"]) == 2


def test_list_experiments():
    with TestClient(app) as client:
        res = client.get("/api/experiments")
        assert res.status_code == 200
        assert "items" in res.json()


def test_delete_simulation():
    with TestClient(app) as client:
        data = create(client)
        res = client.delete(f"/api/simulations/{data['id']}")
        assert res.status_code == 200
        assert res.json()["deleted"] is True
        res = client.get(f"/api/simulations/{data['id']}")
        assert res.status_code == 404


def test_bad_create_validation():
    with TestClient(app) as client:
        res = client.post("/api/simulations", json=body(flight_count=0))
        assert res.status_code == 422


def test_bad_tick_validation():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/tick", json={"ticks": 0})
        assert res.status_code == 422


def test_bad_runway_close():
    with TestClient(app) as client:
        data = create(client)
        res = client.post(f"/api/simulations/{data['id']}/runways/missing/close", json={"ticks": 2, "reason": "test"})
        assert res.status_code == 404


def test_missing_flight():
    with TestClient(app) as client:
        data = create(client)
        res = client.get(f"/api/simulations/{data['id']}/flights/missing")
        assert res.status_code == 404
