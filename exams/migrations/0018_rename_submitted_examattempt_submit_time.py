# Generated by Django 3.2.5 on 2021-08-05 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0017_auto_20210804_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examattempt',
            old_name='submitted',
            new_name='submit_time',
        ),
    ]