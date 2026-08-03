from alembic import context
from sqlalchemy import engine_from_config, pool
from app.db.base import A
import app.db.tables

a = context.config
b = A.metadata

def c():
    d = a.get_main_option("sqlalchemy.url")
    context.configure(url=d, target_metadata=b, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def e():
    f = engine_from_config(a.get_section(a.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
    with f.connect() as g:
        context.configure(connection=g, target_metadata=b)
        with context.begin_transaction():
            context.run_migrations()

c() if context.is_offline_mode() else e()
