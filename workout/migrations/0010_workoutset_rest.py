# Generated by Django 3.1.8 on 2021-06-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_auto_20210620_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutset',
            name='rest',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]