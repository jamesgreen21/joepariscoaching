# Generated by Django 3.1.8 on 2021-04-21 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='name',
            new_name='subject',
        ),
    ]
