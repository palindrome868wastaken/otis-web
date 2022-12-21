# Generated by Django 3.2.5 on 2021-08-05 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0033_auto_20210804_2035"),
        ("roster", "0062_student_achievements"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="achievements",
            field=models.ManyToManyField(
                blank=True,
                help_text="Codes that this student has obtained",
                to="dashboard.Achievement",
            ),
        ),
    ]
