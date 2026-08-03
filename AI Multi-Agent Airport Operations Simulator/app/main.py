from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.core.config import a
from app.core.log import a as logx
from app.core.obs import b
from app.api.routes import a as r
from app.db.base import A
from app.db.session import b as eng
import app.db.tables

logx()
c = FastAPI(title=a.app_name, version="1.0.0")
c.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
c.include_router(r)
Instrumentator().instrument(c).expose(c)
b(c)

@c.on_event("startup")
def d():
    A.metadata.create_all(eng)

@c.get("/health")
def e():
    return {"ok": True, "name": a.app_name}

app = c
