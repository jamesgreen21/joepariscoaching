# Generated by Django 3.1.8 on 2021-06-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0023_journal_checkin_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='weight_targetted',
        ),
        migrations.AlterField(
            model_name='progress',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]