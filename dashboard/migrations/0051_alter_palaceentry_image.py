# Generated by Django 3.2.7 on 2021-09-17 01:13

import dashboard.models
import rpg.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0050_auto_20210916_2110"),
    ]

    operations = [
        migrations.AlterField(
            model_name="palaceentry",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Optional small photo that will appear next to your entry",
                null=True,
                upload_to=rpg.models.achievement_image_file_name,
                validators=[dashboard.models.validate_at_most_1mb],
            ),
        ),
    ]
