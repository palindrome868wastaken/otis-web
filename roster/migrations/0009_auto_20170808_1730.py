# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 22:30
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("roster", "0008_auto_20170806_0053"),
    ]

    operations = [
        migrations.RenameModel("TA", "Assistant"),
        migrations.AlterField(
            model_name="assistant",
            name="name",
            field=models.CharField(
                help_text="The display name for this Assistant (e.g. a nickname)",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="semester",
            field=models.ForeignKey(
                help_text="The semester for this Assistant",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.Semester",
            ),
        ),
        migrations.AlterField(
            model_name="assistant",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="The Django Auth user attached to the Assistant",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="assistant",
            field=models.ForeignKey(
                blank=True,
                help_text="The Assistant for this student, if any",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="roster.Assistant",
            ),
        ),
    ]
