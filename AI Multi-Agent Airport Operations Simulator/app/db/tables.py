import uuid
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, JSON, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import A

class B(A):
    __tablename__ = "simulations"
    a: Mapped[str] = mapped_column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    b: Mapped[str] = mapped_column("name", String(120))
    c: Mapped[str] = mapped_column("mode", String(30))
    d: Mapped[int] = mapped_column("seed", Integer)
    e: Mapped[str] = mapped_column("status", String(30), default="created")
    f: Mapped[dict] = mapped_column("config", JSON, default=dict)
    g: Mapped[datetime] = mapped_column("created_at", DateTime, default=datetime.utcnow)

class C(A):
    __tablename__ = "events"
    a: Mapped[str] = mapped_column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    b: Mapped[str] = mapped_column("simulation_id", ForeignKey("simulations.id"), index=True)
    c: Mapped[int] = mapped_column("simulation_time", Integer)
    d: Mapped[str] = mapped_column("event_type", String(80))
    e: Mapped[str] = mapped_column("source", String(120))
    f: Mapped[dict] = mapped_column("payload", JSON)
    g: Mapped[datetime] = mapped_column("created_at", DateTime, default=datetime.utcnow)

class D(A):
    __tablename__ = "experiments"
    a: Mapped[str] = mapped_column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    b: Mapped[str] = mapped_column("name", String(120))
    c: Mapped[int] = mapped_column("runs", Integer)
    d: Mapped[dict] = mapped_column("result", JSON)
    e: Mapped[datetime] = mapped_column("created_at", DateTime, default=datetime.utcnow)

class E(A):
    __tablename__ = "ai_decisions"
    a: Mapped[str] = mapped_column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    b: Mapped[str] = mapped_column("simulation_id", String(36), index=True)
    c: Mapped[str] = mapped_column("input", String)
    d: Mapped[str] = mapped_column("output", String)
    e: Mapped[float] = mapped_column("latency_ms", Float)
    f: Mapped[datetime] = mapped_column("created_at", DateTime, default=datetime.utcnow)
