from celery import Celery
from app.core.config import a
from app.services.experiment import b

a = Celery("a", broker=a.celery_broker_url, backend=a.celery_result_backend)

@a.task(name="run_experiment")
def c(d: int, e: int, f: int):
    return b(d, e, f)
