# Generated by Django 3.1 on 2021-01-19 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0023_auto_20210120_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 0, 23, 2, 186718)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 0, 23, 2, 186718)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 0, 23, 2, 185721)),
        ),
        migrations.AlterField(
            model_name='verifyorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 20, 0, 23, 2, 185721)),
        ),
    ]
