# Generated by Django 3.1.8 on 2021-04-24 13:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_auto_20210424_1453'),
        ('journal', '0008_auto_20210424_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 24, 13, 53, 1, 505582, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.IntegerField(blank=True, help_text='Reps', null=True)),
                ('weight_targetted', models.IntegerField(blank=True, null=True, verbose_name='Weight in KG')),
                ('weight', models.IntegerField(blank=True, help_text='Weight in KG', null=True)),
                ('approach_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workout.approach', verbose_name='Approach')),
                ('journal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.journal', verbose_name='Journal')),
            ],
        ),
    ]