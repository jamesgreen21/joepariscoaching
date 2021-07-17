# Generated by Django 3.1.8 on 2021-06-20 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_auto_20210620_1540'),
        ('journal', '0027_progress_workoutset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='approach_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='progress', to='workout.approach'),
        ),
    ]