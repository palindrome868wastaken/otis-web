# Generated by Django 3.2.8 on 2021-10-31 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("markets", "0009_alter_market_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="market",
            name="solution",
            field=models.TextField(
                blank=True, help_text="Comments that appear in the market results."
            ),
        ),
    ]
