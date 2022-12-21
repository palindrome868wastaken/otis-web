# Generated by Django 4.0.8 on 2022-11-15 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0081_delete_problemsuggestion"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="achievement",
                    name="creator",
                ),
                migrations.AlterUniqueTogether(
                    name="achievementunlock",
                    unique_together=None,
                ),
                migrations.RemoveField(
                    model_name="achievementunlock",
                    name="achievement",
                ),
                migrations.RemoveField(
                    model_name="achievementunlock",
                    name="user",
                ),
                migrations.RemoveField(
                    model_name="bonuslevel",
                    name="group",
                ),
                migrations.RemoveField(
                    model_name="bonuslevelunlock",
                    name="bonus",
                ),
                migrations.RemoveField(
                    model_name="bonuslevelunlock",
                    name="student",
                ),
                migrations.DeleteModel(
                    name="Level",
                ),
                migrations.RemoveField(
                    model_name="palacecarving",
                    name="user",
                ),
                migrations.RemoveField(
                    model_name="questcomplete",
                    name="student",
                ),
                migrations.DeleteModel(
                    name="Achievement",
                ),
                migrations.DeleteModel(
                    name="AchievementUnlock",
                ),
                migrations.DeleteModel(
                    name="BonusLevel",
                ),
                migrations.DeleteModel(
                    name="BonusLevelUnlock",
                ),
                migrations.DeleteModel(
                    name="PalaceCarving",
                ),
                migrations.DeleteModel(
                    name="QuestComplete",
                ),
            ],
            database_operations=[],
        )
    ]
