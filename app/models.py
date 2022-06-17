import requests
from django.conf import settings
from django.db import models
from django.utils.datetime_safe import datetime

from app.config import DAYS_OF_WEEK_CHOICES


class AlterEC2Request(models.Model):
    """
    Contains all the EC2 alteration requests. The request can contain
    various number of arguments.

    Arguments Example:
        1. Instance Type
        2. Storage IOPS
        3. Storage Space

    For now, this handles only the `instance_type`.
    """

    name = models.CharField(max_length=255)

    day_of_action = models.PositiveIntegerField(
        choices=DAYS_OF_WEEK_CHOICES, default=DAYS_OF_WEEK_CHOICES[0][0]
    )
    time_of_action = models.TimeField()

    instance_for_action = models.CharField(max_length=255)
    instance_name = models.CharField(max_length=255)
    change_to_instance_type = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def handle_started(self):
        """
        Handles the fact that the scheduled time for the request has come.
        Creates the necessary logs and returns the same.
        """

        post_on_slack_channel(
            message=f"Processing request `{self.name}`, changing instance to `{self.change_to_instance_type}`."
        )
        return AlterEC2Log.objects.create(for_request=self)


class AlterEC2Log(models.Model):
    """Just a log for `AlterEC2Request`. Represented to the user."""

    started_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(default=None, null=True)

    status = models.CharField(
        max_length=10,
        choices=(
            ("processing", "Processing"),
            ("success", "Success"),
            ("failure", "Failure"),
        ),
        default="processing",
    )
    error = models.TextField(default=None, null=True)

    for_request = models.ForeignKey(
        to=AlterEC2Request,
        on_delete=models.CASCADE,
        related_name="related_alter_ec2_logs",
    )

    def handle_success(self):
        """Handles the fact that the request is completed successfully."""

        self.completed_on = datetime.now()
        self.status = "success"
        self.error = None
        self.save()

        post_on_slack_channel(
            message=f"Request `{self.for_request.name}` succeeded :tada:"
        )

    def handle_error(self, error: str):
        """Handles the fact that the request has completed with an error."""

        self.completed_on = datetime.now()
        self.status = "failure"
        self.error = error
        self.save()

        post_on_slack_channel(
            message=f"Request `{self.for_request.name}` failed :cry:\nError: `{self.error}`"
        )


def post_on_slack_channel(message: str) -> (bool, str):
    """
    Given the message, this will post the message on the Slack
    channel configured on the settings.py file.

    Used on init and end of the scheduled request. Returns
    (is_success, error) to the caller.
    """

    try:
        requests.post(
            url="https://slack.com/api/chat.postMessage",
            data={"channel": settings.SLACK_NOTIFY_CHANNEL_ID, "text": message},
            headers={
                "Authorization": f"Bearer {settings.SLACK_NOTIFY_BOT_ACCESS_TOKEN}"
            },
        )

        return True, None
    except Exception as e:
        return False, str(e)
