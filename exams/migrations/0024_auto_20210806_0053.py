# Generated by Django 3.2.5 on 2021-08-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0023_remove_practiceexam_pdf_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examattempt",
            name="guess1",
            field=models.CharField(
                default="", max_length=36, verbose_name="Problem 1 response"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess2",
            field=models.CharField(
                default="", max_length=36, verbose_name="Problem 2 response"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess3",
            field=models.CharField(
                default="", max_length=36, verbose_name="Problem 3 response"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess4",
            field=models.CharField(
                default="", max_length=36, verbose_name="Problem 4 response"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess5",
            field=models.CharField(
                default="", max_length=36, verbose_name="Problem 5 response"
            ),
            preserve_default=False,
        ),
    ]
