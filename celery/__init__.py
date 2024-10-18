from celery import Celery

from api.src.config import settings

app = Celery(
    "ai_request_handler",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.conf.update(
    task_serializer="json",
    accept_content=["application/json"],
    result_serializer="json",
    task_track_started=True,
    task_time_limit=300,
    task_soft_time_limit=60,
    worker_prefetch_multiplier=1,
    result_expires=3600,
)

if __name__ == "__main__":
    app.start()