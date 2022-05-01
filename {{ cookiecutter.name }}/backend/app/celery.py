import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery(broker=settings.CELERY_BROKER_URL)
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()


# if not settings.DEBUG:
#     app.conf.beat_schedule = {}
# app.conf.task_routes = {}


if __name__ == "__main__":
    app.start()
