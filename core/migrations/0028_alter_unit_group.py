# Generated by Django 3.2.6 on 2021-08-10 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_alter_semester_uses_legacy_pset_system"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unit",
            name="group",
            field=models.ForeignKey(
                default=1,
                help_text="The group that this unit belongs to",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.unitgroup",
            ),
            preserve_default=False,
        ),
    ]
