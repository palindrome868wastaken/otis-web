# Generated by Django 3.2.8 on 2021-10-27 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0067_alter_achievement_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achievement",
            name="code",
            field=models.CharField(
                max_length=96,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="24-25 char hex string", regex="^[a-f0-9]{24,25}$"
                    )
                ],
            ),
        ),
    ]
