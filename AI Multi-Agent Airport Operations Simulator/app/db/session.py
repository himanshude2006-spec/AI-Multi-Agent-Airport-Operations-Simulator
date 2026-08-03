from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import a

b = create_engine(a.database_url)
c = sessionmaker(bind=b, autoflush=False, autocommit=False)

def d():
    e = c()
    try:
        yield e
    finally:
        e.close()
