# Generated by Django 3.1.8 on 2021-05-03 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0012_progress_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='is_active',
        ),
    ]