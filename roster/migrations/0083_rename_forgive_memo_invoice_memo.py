# Generated by Django 3.2.12 on 2022-02-19 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0082_student_enabled"),
    ]

    operations = [
        migrations.RenameField(
            model_name="invoice",
            old_name="forgive_memo",
            new_name="memo",
        ),
    ]
