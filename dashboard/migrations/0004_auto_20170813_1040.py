# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_auto_20170810_2209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="file_type",
            field=models.CharField(
                choices=[
                    ("HMWK", "PSet Submission"),
                    ("TRNS", "Transcript"),
                    ("NOTE", "Notes / Comments"),
                    ("MISC", "Miscellaneous"),
                ],
                help_text="What kind of file this is",
                max_length=10,
            ),
        ),
    ]
