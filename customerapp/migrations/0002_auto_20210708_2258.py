# Generated by Django 3.1.6 on 2021-07-08 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 22, 58, 0, 501510)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 22, 58, 0, 502508)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 22, 58, 0, 497519)),
        ),
        migrations.AlterField(
            model_name='verifyorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 22, 58, 0, 500513)),
        ),
    ]
