from django.db import models

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
    change_to_instance_type = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


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
