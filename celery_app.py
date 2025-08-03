from celery import Celery
import os

BROKER = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")


celery_app = Celery("celery_app", broker=BROKER, backend=BACKEND, include=["tasks"])


celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Tokyo",
    task_track_started=True,
)