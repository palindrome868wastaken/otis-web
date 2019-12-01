# Generated by Django 2.1.11 on 2019-12-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190830_1219'),
        ('roster', '0030_auto_20191201_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pointer_current_unit',
        ),
        migrations.AddField(
            model_name='student',
            name='extra_units',
            field=models.ManyToManyField(blank=True, help_text='A list of units that the student can access out-of-order relative to their curriculum.', related_name='extra_units', to='core.Unit'),
        ),
        migrations.AlterField(
            model_name='student',
            name='curriculum',
            field=models.ManyToManyField(blank=True, help_text='The choice of units that this student will work on', related_name='curriculum', to='core.Unit'),
        ),
        migrations.AlterField(
            model_name='unitinquiry',
            name='action_type',
            field=models.CharField(choices=[('DROP', 'Drop'), ('ADD', 'Add')], help_text='Describe the action you want to make.', max_length=10),
        ),
    ]
