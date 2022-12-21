# Generated by Django 3.2.8 on 2021-10-22 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0080_auto_20211020_0923"),
        ("exams", "0027_auto_20210806_0955"),
    ]

    operations = [
        migrations.CreateModel(
            name="MockCompleted",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="roster.student"
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exams.practiceexam",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "test")},
            },
        ),
    ]
