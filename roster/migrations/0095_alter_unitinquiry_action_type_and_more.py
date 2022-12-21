# Generated by Django 4.0.8 on 2022-12-15 01:27

from django.db import migrations, models
from typing import Any

ACTION_CHOICES = (
    ("UNLOCK", "INQ_ACT_UNLOCK"),
    ("APPEND", "INQ_ACT_APPEND"),
    ("DROP", "INQ_ACT_DROP"),
)
STATUS_CHOICES = (
    ("ACC", "INQ_ACC"),
    ("REJ", "INQ_REJ"),
    ("NEW", "INQ_NEW"),
    ("HOLD", "INQ_HOLD"),
)


def update_fields(apps: Any, scheme_editor: Any):
    UnitInquiry = apps.get_model("roster", "unitinquiry")
    for x, y in ACTION_CHOICES:
        UnitInquiry.objects.filter(action_type=x).update(action_type=y)
    for x, y in STATUS_CHOICES:
        UnitInquiry.objects.filter(status=x).update(status=y)


def revert_fields(apps: Any, scheme_editor: Any):
    UnitInquiry = apps.get_model("roster", "unitinquiry")
    for y, x in ACTION_CHOICES:
        UnitInquiry.objects.filter(action_type=x).update(action_type=y)
    for y, x in STATUS_CHOICES:
        UnitInquiry.objects.filter(status=x).update(status=y)


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0094_invoice_credits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitinquiry",
            name="action_type",
            field=models.CharField(
                choices=[
                    ("INQ_ACT_UNLOCK", "Unlock now"),
                    ("INQ_ACT_APPEND", "Add for later"),
                    ("INQ_ACT_DROP", "Drop"),
                ],
                help_text="Describe the action you want to make.",
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="unitinquiry",
            name="status",
            field=models.CharField(
                choices=[
                    ("INQ_ACC", "Accepted"),
                    ("INQ_REJ", "Rejected"),
                    ("INQ_NEW", "Pending"),
                    ("INQ_HOLD", "On hold"),
                ],
                default="INQ_NEW",
                help_text="The current status of the petition.",
                max_length=10,
            ),
        ),
        migrations.RunPython(update_fields, revert_fields),
    ]
