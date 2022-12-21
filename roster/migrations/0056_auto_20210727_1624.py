# Generated by Django 3.2.5 on 2021-07-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0055_auto_20210727_1609"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentregistration",
            name="name",
        ),
        migrations.AddField(
            model_name="studentregistration",
            name="first_name",
            field=models.CharField(
                default="", help_text="Your first name", max_length=1282
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentregistration",
            name="last_name",
            field=models.CharField(
                default="", help_text="Your last name", max_length=128
            ),
            preserve_default=False,
        ),
    ]
