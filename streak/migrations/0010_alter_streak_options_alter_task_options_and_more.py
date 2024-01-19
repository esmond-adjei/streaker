# Generated by Django 5.0.1 on 2024-01-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streak', '0009_alter_streak_options_alter_task__completion_period_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streak',
            options={'ordering': ['task', '-created_at']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='streak',
            name='day_count',
            field=models.PositiveIntegerField(default=1, editable=False),
        ),
    ]
