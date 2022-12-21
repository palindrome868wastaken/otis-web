# Generated by Django 3.0.7 on 2021-02-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0049_auto_20210111_1623"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="extras",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Additional payment, e.g. for T-shirts.",
                max_digits=8,
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="adjustment",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Adjustment to the cost, e.g. for financial aid.",
                max_digits=8,
            ),
        ),
    ]
