# Generated by Django 3.1.8 on 2021-05-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0011_auto_20210502_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]