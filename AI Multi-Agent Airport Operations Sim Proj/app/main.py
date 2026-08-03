from __future__ import annotations

import asyncio
import logging
import time
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.web.api import router
from app.data.db import database
from app.airport.engine import engine_store
from app.web.events import bus
from app.other.settings import settings
from app.data.store import store


logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO), format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger("airport")


@asynccontextmanager
async def life(app: FastAPI):
    db_ok = False
    if settings.use_database:
        db_ok = await asyncio.to_thread(database.start)
    store_result = await store.start()
    event_ok = await bus.start()
    app.state.started_at = time.time()
    app.state.database_ok = db_ok
    app.state.store_result = store_result
    app.state.event_ok = event_ok
    log.info("application started")
    yield
    await bus.stop()
    await store.stop()
    if settings.use_database:
        await asyncio.to_thread(database.stop)
    await bus.hub.close_all()
    log.info("application stopped")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend-only multi-agent airport operations simulator",
    lifespan=life,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


origins = [x.strip() for x in settings.allowed_origins.split(",") if x.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def request_time(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception as exc:
        log.exception("request failed")
        return JSONResponse(status_code=500, content={"detail": str(exc), "path": request.url.path})
    took = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{took:.6f}"
    response.headers["X-App-Name"] = settings.app_name
    return response


@app.exception_handler(KeyError)
async def key_error(request: Request, exc: KeyError):
    return JSONResponse(status_code=404, content={"detail": "item not found", "item": str(exc), "path": request.url.path})


@app.exception_handler(ValueError)
async def value_error(request: Request, exc: ValueError):
    return JSONResponse(status_code=422, content={"detail": str(exc), "path": request.url.path})


@app.get("/")
async def root() -> dict[str, Any]:
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "backend_only": True,
        "docs": "/docs",
        "api": settings.api_prefix,
        "websocket": f"{settings.api_prefix}/ws/{{simulation_id}}",
        "status": "running",
    }


@app.get("/health")
async def top_health() -> dict[str, Any]:
    started = getattr(app.state, "started_at", time.time())
    return {
        "ok": True,
        "name": settings.app_name,
        "version": settings.app_version,
        "uptime_seconds": round(time.time() - started, 3),
        "database_ok": getattr(app.state, "database_ok", False),
        "event_ok": getattr(app.state, "event_ok", False),
        "store": getattr(app.state, "store_result", {}),
        "engines": engine_store.stats(),
        "events": bus.stats(),
    }


@app.get("/about")
async def about() -> dict[str, Any]:
    return {
        "project": "AI Multi-Agent Airport Operations Simulator",
        "type": "backend simulation platform",
        "components": [
            "FastAPI REST API",
            "simulation engine",
            "flight agents",
            "runway agents",
            "gate agents",
            "weather agent",
            "event bus",
            "WebSocket stream",
            "PostgreSQL persistence",
            "Redis cache and pubsub",
            "Celery jobs",
            "OR-Tools scheduler",
            "OpenAI advisory layer",
            "Pytest tests",
        ],
        "frontend": False,
    }


@app.get("/runtime")
async def runtime() -> dict[str, Any]:
    return {
        "settings": {
            "database": settings.use_database,
            "redis": settings.use_redis,
            "celery": settings.use_celery,
            "ai": settings.use_ai,
            "max_simulations": settings.max_simulations,
            "max_events": settings.max_events_per_sim,
            "snapshot_gap": settings.snapshot_gap,
        },
        "engines": engine_store.stats(),
        "events": bus.stats(),
        "database": database.stats(),
        "store": store.stats(),
    }


app.include_router(router, prefix=settings.api_prefix)


def get_app() -> FastAPI:
    return app


def app_info() -> dict[str, Any]:
    return {
        "title": app.title,
        "version": app.version,
        "routes": len(app.routes),
        "debug": app.debug,
        "api_prefix": settings.api_prefix,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.app_host, port=settings.app_port, reload=settings.app_debug)
