# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-07 14:11
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_semester_show_invoices"),
        ("roster", "0015_auto_20171205_0939"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ("-legit", "name")},
        ),
        migrations.AddField(
            model_name="student",
            name="pointer_current_unit",
            field=models.ForeignKey(
                blank=True,
                help_text="If set, the counter will skip ahead so that the student is working on this unit instead.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pointer_unit",
                to="core.Unit",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="current_unit_index",
            field=models.SmallIntegerField(
                default=0,
                help_text="If this is equal to k, then the student has completed the first k units of his/her curriculum and by default is working on the (k+1)st unit.",
            ),
        ),
    ]
