# Generated by Django 3.2.5 on 2021-07-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0054_auto_20210727_1603"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentregistration",
            name="grade_level",
        ),
        migrations.AddField(
            model_name="registrationcontainer",
            name="end_year",
            field=models.IntegerField(
                default=2022, help_text="The year in which OTIS will end"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentregistration",
            name="graduation_year",
            field=models.IntegerField(
                choices=[
                    (0, "Already graduated high school"),
                    (2022, "Graduating in 2022"),
                    (2023, "Graduating in 2023"),
                    (2024, "Graduating in 2024"),
                    (2025, "Graduating in 2025"),
                    (2026, "Graduating in 2026"),
                    (2027, "Graduating in 2027"),
                    (2028, "Graduating in 2028"),
                    (2029, "Graduating in 2029"),
                ],
                default=0,
                help_text="Enter your expected graduation year",
            ),
            preserve_default=False,
        ),
    ]
