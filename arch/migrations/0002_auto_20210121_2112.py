# Generated by Django 3.0.7 on 2021-01-22 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_auto_20200908_1307"),
        ("arch", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hint",
            options={"ordering": ("number",)},
        ),
        migrations.RenameField(
            model_name="hint",
            old_name="numbers",
            new_name="number",
        ),
        migrations.CreateModel(
            name="Problem",
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
                    "source",
                    models.CharField(
                        blank=True,
                        help_text="The source of the problem, such as `TSTST 2020/3`.If in doubt on formatting, follow what is written on the handout.",
                        max_length=255,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A short description of the problem, e.g. `Quirky triangles.`. Most important if the problem does not have a source given. Use sentence case.",
                        max_length=255,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The unit to which this problem belongs.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.UnitGroup",
                    ),
                ),
            ],
            options={
                "ordering": ("source", "description"),
            },
        ),
        migrations.AddField(
            model_name="hint",
            name="problem",
            field=models.ForeignKey(
                default=None,
                help_text="The container of the current hint.",
                on_delete=django.db.models.deletion.CASCADE,
                to="arch.Problem",
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name="hint",
            unique_together={("problem", "number")},
        ),
        migrations.RemoveField(
            model_name="hint",
            name="group",
        ),
        migrations.RemoveField(
            model_name="hint",
            name="problem_source",
        ),
    ]
