import random
from datetime import timedelta

from django.conf import settings
from django.utils.datetime_safe import datetime

from app.aws_ec2 import change_instance_type
from app.models import AlterEC2Request
from config.celery_app import app as celery_app


@celery_app.task
def request_scheduler_beat_task():
    """The beat task to run the necessary requests on schedule."""

    now = datetime.now()
    before = now - timedelta(minutes=15)
    after = now + timedelta(minutes=15)

    qs = AlterEC2Request.objects.filter(
        time_of_action__gte=before,
        time_of_action__lte=after,
        day_of_action=now.weekday(),
    )

    for request in qs:
        log = request.handle_started()

        # check if the ec2 actions are to be performed or not
        if settings.REQUEST_SCHEDULER_PERFORM_EC2_ACTIONS:
            is_success, error = change_instance_type(
                instance_id=request.instance_for_action,
                instance_type=request.change_to_instance_type,
            )
        else:
            is_success, error = random.choice([(True, None), (False, "Dummy Error")])

        # condition based notifications
        if is_success:
            log.handle_success()
        else:
            log.handle_error(error=error)
