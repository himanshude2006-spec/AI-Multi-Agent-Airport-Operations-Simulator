import asyncio
from dataclasses import asdict
from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from app.api.schemas import A, B, C1, D
from app.services.store import e
from app.api.ws import h
from app.services.experiment import b as runx
from app.ai.flow import l
from app.worker import c as task

a = APIRouter()

@a.post("/simulations")
async def b(c: A):
    d = e.b(c.a, c.b, c.c)
    return d.s()

@a.get("/simulations/{c}")
async def d(c: str):
    f = e.c(c)
    if not f:
        raise HTTPException(404, "not found")
    return f.s()

@a.post("/simulations/{c}/step")
async def g(c: str, d: B):
    f = e.c(c)
    if not f:
        raise HTTPException(404, "not found")
    x = []
    for _ in range(d.a):
        y = f.q()
        x.extend(asdict(z) for z in y)
        await h.d(c, {"type": "tick", "state": f.s(), "events": [asdict(z) for z in y]})
    return {"state": f.s(), "events": x}

@a.post("/experiments/run")
async def i(c: C1):
    return runx(c.a, c.b, c.c)

@a.post("/experiments/queue")
async def j(c: C1):
    d = task.delay(c.a, c.b, c.c)
    return {"task_id": d.id}

@a.get("/experiments/tasks/{c}")
async def k(c: str):
    d = task.AsyncResult(c)
    return {"id": c, "state": d.state, "result": d.result if d.ready() else None}

@a.post("/ai/advice")
async def m(c: D):
    return await l.ainvoke({"a": {"kind": c.a, **c.b}, "b": None, "c": False, "d": None})

@a.websocket("/ws/{c}")
async def n(c: str, d: WebSocket):
    await h.b(c, d)
    try:
        while True:
            await d.receive_text()
    except WebSocketDisconnect:
        h.c(c, d)
