from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Iterator

from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text, create_engine, delete, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.settings import settings
from app.types import Experiment, SimEvent, SimState


def now_time() -> datetime:
    return datetime.now(timezone.utc)


def json_text(data: Any) -> str:
    return json.dumps(data, default=str, separators=(",", ":"))


def json_data(text: str | None, default: Any) -> Any:
    if not text:
        return default
    try:
        return json.loads(text)
    except Exception:
        return default


class Base(DeclarativeBase):
    pass


class SimRow(Base):
    __tablename__ = "simulations"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(200), default="Airport Test")
    status: Mapped[str] = mapped_column(String(40), default="created", index=True)
    algorithm: Mapped[str] = mapped_column(String(40), default="weighted", index=True)
    seed: Mapped[int] = mapped_column(Integer, default=42)
    tick: Mapped[int] = mapped_column(Integer, default=0)
    flight_count: Mapped[int] = mapped_column(Integer, default=0)
    runway_count: Mapped[int] = mapped_column(Integer, default=0)
    gate_count: Mapped[int] = mapped_column(Integer, default=0)
    completed_count: Mapped[int] = mapped_column(Integer, default=0)
    diverted_count: Mapped[int] = mapped_column(Integer, default=0)
    average_delay: Mapped[float] = mapped_column(Float, default=0.0)
    overall_score: Mapped[float] = mapped_column(Float, default=0.0)
    config_json: Mapped[str] = mapped_column(Text, default="{}")
    state_json: Mapped[str] = mapped_column(Text, default="{}")
    metrics_json: Mapped[str] = mapped_column(Text, default="{}")
    done_reason: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time, onupdate=now_time)

    @classmethod
    def from_state(cls, state: SimState) -> SimRow:
        return cls(
            id=state.id,
            name=state.config.name,
            status=state.status,
            algorithm=state.config.algorithm.value,
            seed=state.config.seed,
            tick=state.tick,
            flight_count=len(state.flights),
            runway_count=len(state.runways),
            gate_count=len(state.gates),
            completed_count=state.metrics.completed,
            diverted_count=state.metrics.diverted,
            average_delay=state.metrics.average_delay,
            overall_score=state.metrics.overall_score,
            config_json=json_text(state.config.to_dict()),
            state_json=json_text(state.to_dict()),
            metrics_json=json_text(state.metrics.to_dict()),
            done_reason=state.done_reason,
            created_at=parse_time(state.created_at),
            updated_at=parse_time(state.updated_at),
        )

    def update_from_state(self, state: SimState) -> None:
        self.name = state.config.name
        self.status = state.status
        self.algorithm = state.config.algorithm.value
        self.seed = state.config.seed
        self.tick = state.tick
        self.flight_count = len(state.flights)
        self.runway_count = len(state.runways)
        self.gate_count = len(state.gates)
        self.completed_count = state.metrics.completed
        self.diverted_count = state.metrics.diverted
        self.average_delay = state.metrics.average_delay
        self.overall_score = state.metrics.overall_score
        self.config_json = json_text(state.config.to_dict())
        self.state_json = json_text(state.to_dict())
        self.metrics_json = json_text(state.metrics.to_dict())
        self.done_reason = state.done_reason
        self.updated_at = now_time()

    def to_state(self) -> SimState:
        return SimState.from_dict(json_data(self.state_json, {}))

    def to_dict(self, include_state: bool = False) -> dict[str, Any]:
        data = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "algorithm": self.algorithm,
            "seed": self.seed,
            "tick": self.tick,
            "flight_count": self.flight_count,
            "runway_count": self.runway_count,
            "gate_count": self.gate_count,
            "completed_count": self.completed_count,
            "diverted_count": self.diverted_count,
            "average_delay": self.average_delay,
            "overall_score": self.overall_score,
            "done_reason": self.done_reason,
            "created_at": self.created_at.isoformat() if self.created_at else "",
            "updated_at": self.updated_at.isoformat() if self.updated_at else "",
        }
        if include_state:
            data["state"] = json_data(self.state_json, {})
            data["config"] = json_data(self.config_json, {})
            data["metrics"] = json_data(self.metrics_json, {})
        return data


class EventRow(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    sim_id: Mapped[str] = mapped_column(String(50), index=True)
    tick: Mapped[int] = mapped_column(Integer, default=0, index=True)
    kind: Mapped[str] = mapped_column(String(80), index=True)
    text: Mapped[str] = mapped_column(Text, default="")
    data_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time)

    @classmethod
    def from_event(cls, item: SimEvent) -> EventRow:
        return cls(id=item.id, sim_id=item.sim_id, tick=item.tick, kind=item.kind.value, text=item.text, data_json=json_text(item.data))

    def to_event(self) -> SimEvent:
        return SimEvent.from_dict({"id": self.id, "sim_id": self.sim_id, "tick": self.tick, "kind": self.kind, "text": self.text, "data": json_data(self.data_json, {})})

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "sim_id": self.sim_id, "tick": self.tick, "kind": self.kind, "text": self.text, "data": json_data(self.data_json, {}), "created_at": self.created_at.isoformat() if self.created_at else ""}


class ExperimentRow(Base):
    __tablename__ = "experiments"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    name: Mapped[str] = mapped_column(String(200), default="Experiment")
    status: Mapped[str] = mapped_column(String(40), default="created", index=True)
    runs: Mapped[int] = mapped_column(Integer, default=1)
    algorithms_json: Mapped[str] = mapped_column(Text, default="[]")
    config_json: Mapped[str] = mapped_column(Text, default="{}")
    data_json: Mapped[str] = mapped_column(Text, default="{}")
    summary_json: Mapped[str] = mapped_column(Text, default="{}")
    winner: Mapped[str] = mapped_column(String(40), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time, onupdate=now_time)

    @classmethod
    def from_experiment(cls, item: Experiment) -> ExperimentRow:
        return cls(
            id=item.id,
            name=item.name,
            status=item.status,
            runs=item.runs,
            algorithms_json=json_text([x.value for x in item.algorithms]),
            config_json=json_text(item.base_config.to_dict()),
            data_json=json_text(item.to_dict()),
            summary_json=json_text(item.summary),
            winner=str(item.summary.get("winner", "")),
            created_at=parse_time(item.created_at),
            updated_at=parse_time(item.updated_at),
        )

    def update_from_experiment(self, item: Experiment) -> None:
        self.name = item.name
        self.status = item.status
        self.runs = item.runs
        self.algorithms_json = json_text([x.value for x in item.algorithms])
        self.config_json = json_text(item.base_config.to_dict())
        self.data_json = json_text(item.to_dict())
        self.summary_json = json_text(item.summary)
        self.winner = str(item.summary.get("winner", ""))
        self.updated_at = now_time()

    def to_experiment(self) -> Experiment:
        return Experiment.from_dict(json_data(self.data_json, {}))

    def to_dict(self, include_data: bool = False) -> dict[str, Any]:
        data = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "runs": self.runs,
            "algorithms": json_data(self.algorithms_json, []),
            "summary": json_data(self.summary_json, {}),
            "winner": self.winner,
            "created_at": self.created_at.isoformat() if self.created_at else "",
            "updated_at": self.updated_at.isoformat() if self.updated_at else "",
        }
        if include_data:
            data["data"] = json_data(self.data_json, {})
            data["config"] = json_data(self.config_json, {})
        return data


class AiRow(Base):
    __tablename__ = "ai_recommendations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sim_id: Mapped[str] = mapped_column(String(50), index=True)
    tick: Mapped[int] = mapped_column(Integer, default=0)
    action: Mapped[str] = mapped_column(String(80), default="none")
    target: Mapped[str] = mapped_column(String(100), default="")
    reason: Mapped[str] = mapped_column(Text, default="")
    accepted: Mapped[bool] = mapped_column(Boolean, default=False)
    applied: Mapped[bool] = mapped_column(Boolean, default=False)
    source: Mapped[str] = mapped_column(String(40), default="local")
    data_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "sim_id": self.sim_id,
            "tick": self.tick,
            "action": self.action,
            "target": self.target,
            "reason": self.reason,
            "accepted": self.accepted,
            "applied": self.applied,
            "source": self.source,
            "data": json_data(self.data_json, {}),
            "created_at": self.created_at.isoformat() if self.created_at else "",
        }


class SnapshotRow(Base):
    __tablename__ = "snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sim_id: Mapped[str] = mapped_column(String(50), index=True)
    tick: Mapped[int] = mapped_column(Integer, index=True)
    data_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_time)

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "sim_id": self.sim_id, "tick": self.tick, "data": json_data(self.data_json, {}), "created_at": self.created_at.isoformat() if self.created_at else ""}


def parse_time(text: str | None) -> datetime:
    if not text:
        return now_time()
    try:
        return datetime.fromisoformat(text)
    except Exception:
        return now_time()


class Database:
    def __init__(self, url: str | None = None) -> None:
        self.url = url or settings.database_url
        args = {"check_same_thread": False} if self.url.startswith("sqlite") else {}
        self.engine = create_engine(self.url, echo=settings.sql_echo, future=True, connect_args=args)
        self.sessions = sessionmaker(bind=self.engine, expire_on_commit=False, class_=Session)
        self.ready = False
        self.saves = 0
        self.reads = 0
        self.errors = 0

    def start(self) -> bool:
        try:
            Base.metadata.create_all(self.engine)
            self.ready = True
            return True
        except Exception:
            self.errors += 1
            self.ready = False
            return False

    def stop(self) -> None:
        self.engine.dispose()
        self.ready = False

    def session(self) -> Iterator[Session]:
        db = self.sessions()
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            self.errors += 1
            raise
        finally:
            db.close()

    def save_sim(self, state: SimState) -> SimState:
        with self.sessions() as db:
            row = db.get(SimRow, state.id)
            if row is None:
                row = SimRow.from_state(state)
                db.add(row)
            else:
                row.update_from_state(state)
            db.commit()
            self.saves += 1
        return state

    def get_sim(self, sim_id: str) -> SimState | None:
        with self.sessions() as db:
            row = db.get(SimRow, sim_id)
            self.reads += 1
            return row.to_state() if row else None

    def list_sims(self, limit: int = 100, offset: int = 0, status: str = "", algorithm: str = "") -> list[dict[str, Any]]:
        with self.sessions() as db:
            stmt = select(SimRow)
            if status:
                stmt = stmt.where(SimRow.status == status)
            if algorithm:
                stmt = stmt.where(SimRow.algorithm == algorithm)
            stmt = stmt.order_by(SimRow.updated_at.desc()).offset(offset).limit(limit)
            vals = list(db.scalars(stmt).all())
            self.reads += 1
            return [x.to_dict() for x in vals]

    def delete_sim(self, sim_id: str) -> bool:
        with self.sessions() as db:
            row = db.get(SimRow, sim_id)
            if row is None:
                return False
            db.execute(delete(EventRow).where(EventRow.sim_id == sim_id))
            db.execute(delete(SnapshotRow).where(SnapshotRow.sim_id == sim_id))
            db.execute(delete(AiRow).where(AiRow.sim_id == sim_id))
            db.delete(row)
            db.commit()
            return True

    def save_event(self, item: SimEvent) -> SimEvent:
        with self.sessions() as db:
            if db.get(EventRow, item.id) is None:
                db.add(EventRow.from_event(item))
                db.commit()
                self.saves += 1
        return item

    def save_events(self, items: list[SimEvent]) -> int:
        count = 0
        with self.sessions() as db:
            for item in items:
                if db.get(EventRow, item.id) is None:
                    db.add(EventRow.from_event(item))
                    count += 1
            db.commit()
            self.saves += count
        return count

    def get_events(self, sim_id: str, limit: int = 100, offset: int = 0, kind: str = "") -> list[SimEvent]:
        with self.sessions() as db:
            stmt = select(EventRow).where(EventRow.sim_id == sim_id)
            if kind:
                stmt = stmt.where(EventRow.kind == kind)
            stmt = stmt.order_by(EventRow.tick.desc(), EventRow.created_at.desc()).offset(offset).limit(limit)
            vals = list(db.scalars(stmt).all())
            self.reads += 1
            vals.reverse()
            return [x.to_event() for x in vals]

    def save_experiment(self, item: Experiment) -> Experiment:
        with self.sessions() as db:
            row = db.get(ExperimentRow, item.id)
            if row is None:
                row = ExperimentRow.from_experiment(item)
                db.add(row)
            else:
                row.update_from_experiment(item)
            db.commit()
            self.saves += 1
        return item

    def get_experiment(self, experiment_id: str) -> Experiment | None:
        with self.sessions() as db:
            row = db.get(ExperimentRow, experiment_id)
            self.reads += 1
            return row.to_experiment() if row else None

    def list_experiments(self, limit: int = 100, offset: int = 0) -> list[dict[str, Any]]:
        with self.sessions() as db:
            stmt = select(ExperimentRow).order_by(ExperimentRow.updated_at.desc()).offset(offset).limit(limit)
            vals = list(db.scalars(stmt).all())
            self.reads += 1
            return [x.to_dict() for x in vals]

    def save_ai(self, sim_id: str, tick: int, data: dict[str, Any]) -> int:
        with self.sessions() as db:
            row = AiRow(
                sim_id=sim_id,
                tick=tick,
                action=str(data.get("action", "none")),
                target=str(data.get("target", "")),
                reason=str(data.get("reason", "")),
                accepted=bool(data.get("accepted", False)),
                applied=bool(data.get("applied", False)),
                source=str(data.get("source", "local")),
                data_json=json_text(data),
            )
            db.add(row)
            db.commit()
            db.refresh(row)
            self.saves += 1
            return row.id

    def get_ai(self, sim_id: str, limit: int = 100) -> list[dict[str, Any]]:
        with self.sessions() as db:
            stmt = select(AiRow).where(AiRow.sim_id == sim_id).order_by(AiRow.created_at.desc()).limit(limit)
            vals = list(db.scalars(stmt).all())
            self.reads += 1
            return [x.to_dict() for x in vals]

    def save_snapshot(self, sim_id: str, tick: int, data: dict[str, Any]) -> int:
        with self.sessions() as db:
            row = SnapshotRow(sim_id=sim_id, tick=tick, data_json=json_text(data))
            db.add(row)
            db.commit()
            db.refresh(row)
            self.saves += 1
            return row.id

    def get_snapshot(self, sim_id: str, tick: int | None = None) -> dict[str, Any] | None:
        with self.sessions() as db:
            stmt = select(SnapshotRow).where(SnapshotRow.sim_id == sim_id)
            if tick is not None:
                stmt = stmt.where(SnapshotRow.tick <= tick)
            stmt = stmt.order_by(SnapshotRow.tick.desc()).limit(1)
            row = db.scalar(stmt)
            self.reads += 1
            return row.to_dict() if row else None

    def counts(self) -> dict[str, int]:
        with self.sessions() as db:
            return {
                "simulations": int(db.scalar(select(func.count()).select_from(SimRow)) or 0),
                "events": int(db.scalar(select(func.count()).select_from(EventRow)) or 0),
                "experiments": int(db.scalar(select(func.count()).select_from(ExperimentRow)) or 0),
                "ai_recommendations": int(db.scalar(select(func.count()).select_from(AiRow)) or 0),
                "snapshots": int(db.scalar(select(func.count()).select_from(SnapshotRow)) or 0),
            }

    def stats(self) -> dict[str, Any]:
        data = {"ready": self.ready, "url": self.url.split("@")[0] if "@" in self.url else self.url, "saves": self.saves, "reads": self.reads, "errors": self.errors}
        if self.ready:
            try:
                data["counts"] = self.counts()
            except Exception:
                data["counts"] = {}
        return data


database = Database()
