# Generated by Django 3.1.8 on 2021-06-20 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0007_auto_20210620_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutset',
            name='instruction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='workout.instructions'),
        ),
        migrations.AlterField(
            model_name='workoutset',
            name='rpe',
            field=models.IntegerField(default=0),
        ),
    ]