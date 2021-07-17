# Generated by Django 3.1.8 on 2021-06-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_instructions_workoutset'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructions',
            name='title',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workoutset',
            name='rpe',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='instructions',
            name='detail',
            field=models.TextField(),
        ),
    ]
