# Generated by Django 3.2.5 on 2021-08-05 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0018_rename_submitted_examattempt_submit_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="practiceexam",
            name="answer1",
            field=models.IntegerField(blank=True, help_text="Answer to p1", null=True),
        ),
        migrations.AddField(
            model_name="practiceexam",
            name="answer2",
            field=models.IntegerField(blank=True, help_text="Answer to p2", null=True),
        ),
        migrations.AddField(
            model_name="practiceexam",
            name="answer3",
            field=models.IntegerField(blank=True, help_text="Answer to p3", null=True),
        ),
        migrations.AddField(
            model_name="practiceexam",
            name="answer4",
            field=models.IntegerField(blank=True, help_text="Answer to p4", null=True),
        ),
        migrations.AddField(
            model_name="practiceexam",
            name="answer5",
            field=models.IntegerField(blank=True, help_text="Answer to p5", null=True),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess1",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Problem 1 response"
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess2",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Problem 2 response"
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess3",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Problem 3 response"
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess4",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Problem 4 response"
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess5",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Problem 5 response"
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="quiz",
            field=models.ForeignKey(
                help_text="The quiz being submitted for",
                on_delete=django.db.models.deletion.CASCADE,
                to="exams.practiceexam",
            ),
        ),
        migrations.DeleteModel(
            name="Quiz",
        ),
    ]
