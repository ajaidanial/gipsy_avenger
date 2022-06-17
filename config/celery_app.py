import os

from celery import Celery
from celery.schedules import crontab

# Celery Worker - normal configurations
# ------------------------------------------------------------------------------

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("gipsy_avenger")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task functions from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "request_scheduler_beat_task": {
        "task": "app.tasks.request_scheduler_beat_task",
        "schedule": crontab(minute="*/30"),  # every 30 minutes
    },
}
