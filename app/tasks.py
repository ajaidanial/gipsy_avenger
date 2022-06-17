from config.celery_app import app as celery_app


@celery_app.task
def request_scheduler_beat_task():
    pass
