# Generated by Django 3.1.8 on 2021-06-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0028_auto_20210620_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='alternative_exercise',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
