# Generated by Django 3.2.9 on 2022-01-26 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("arch", "0023_alter_problem_puid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="problem",
            name="aops_url",
        ),
    ]
