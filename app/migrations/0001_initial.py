# Generated by Django 4.0.5 on 2022-06-16 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AlterEC2Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "day_of_action",
                    models.PositiveIntegerField(
                        choices=[
                            (0, "SUNDAY"),
                            (1, "MONDAY"),
                            (2, "TUESDAY"),
                            (3, "WEDNESDAY"),
                            (4, "THURSDAY"),
                            (5, "FRIDAY"),
                            (6, "SATURDAY"),
                        ],
                        default=0,
                    ),
                ),
                ("time_of_action", models.TimeField()),
                ("instance_for_action", models.CharField(max_length=255)),
                ("change_to_instance_type", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AlterEC2Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("started_on", models.DateTimeField(auto_now_add=True)),
                ("completed_on", models.DateTimeField(default=None, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("processing", "Processing"),
                            ("success", "Success"),
                            ("failure", "Failure"),
                        ],
                        default="processing",
                        max_length=10,
                    ),
                ),
                ("error", models.TextField(default=None, null=True)),
                (
                    "for_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_alter_ec2_logs",
                        to="app.alterec2request",
                    ),
                ),
            ],
        ),
    ]
