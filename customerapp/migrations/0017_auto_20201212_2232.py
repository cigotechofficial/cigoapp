# Generated by Django 3.1 on 2020-12-12 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0016_auto_20201212_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 22, 32, 52, 551618)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 22, 32, 52, 551618)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 22, 32, 52, 550621)),
        ),
    ]
