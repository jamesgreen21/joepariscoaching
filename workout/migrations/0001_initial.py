# Generated by Django 3.1.7 on 2021-04-10 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tooltip', models.TextField(blank=True, null=True)),
                ('bodypart', models.CharField(blank=True, max_length=50, null=True)),
                ('exercise_type', models.CharField(choices=[('ST', 'Strength'), ('EN', 'Endurance'), ('CO', 'Core'), ('FL', 'Flexibility')], default='NA', max_length=2)),
                ('tag', models.TextField(blank=True, null=True)),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workout.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Perform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tag', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('complete', models.BooleanField(default=False)),
                ('exercise_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='workout.exercise', verbose_name='Exercise')),
                ('workout_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout.workout', verbose_name='Workout')),
            ],
        ),
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField(default=1)),
                ('reps_targetted', models.IntegerField(default=0, verbose_name='Reps')),
                ('reps_recorded', models.IntegerField(blank=True, help_text='Reps', null=True)),
                ('duration', models.DecimalField(decimal_places=2, default=0, help_text='Time in Minutes', max_digits=5)),
                ('weight_targetted', models.IntegerField(blank=True, null=True, verbose_name='Weight in KG')),
                ('weight_recorded', models.IntegerField(blank=True, help_text='Weight in KG', null=True)),
                ('perform_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='workout.perform', verbose_name='Perform')),
                ('routine_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workout.routine')),
            ],
        ),
    ]
