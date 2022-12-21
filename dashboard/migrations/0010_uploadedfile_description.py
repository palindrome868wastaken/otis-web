# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0009_auto_20170818_1605"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadedfile",
            name="description",
            field=models.CharField(
                blank=True, help_text="Optional description of the file", max_length=250
            ),
        ),
    ]
