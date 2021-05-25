# Generated by Django 3.1.8 on 2021-05-09 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0005_auto_20210509_1540'),
        ('journal', '0016_auto_20210509_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='journal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='journal.journal'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='approach_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='progress', to='workout.approach', verbose_name='Approach'),
        ),
    ]
