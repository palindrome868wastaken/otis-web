# Generated by Django 3.2.8 on 2021-10-20 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0079_alter_studentregistration_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentregistration",
            options={},
        ),
        migrations.AlterModelOptions(
            name="unitinquiry",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Unit petition",
                "verbose_name_plural": "Unit petitions",
            },
        ),
    ]
