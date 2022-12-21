# Generated by Django 4.0.8 on 2022-11-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0039_alter_semester_calendar_url_meets_evan_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semester",
            name="calendar_url_meets_evan",
            field=models.URLField(
                blank=True,
                help_text="Link to calendar for students with meetings with Evan",
                max_length=1024,
            ),
        ),
        migrations.AlterField(
            model_name="semester",
            name="calendar_url_no_meets_evan",
            field=models.URLField(
                blank=True,
                help_text="Link to calendar for students without meetings with Evan",
                max_length=1024,
            ),
        ),
    ]
