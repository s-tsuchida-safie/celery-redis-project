import time

from celery_app import celery_app


@celery_app.task
def add(x, y):
    time.sleep(2)
    return x + y