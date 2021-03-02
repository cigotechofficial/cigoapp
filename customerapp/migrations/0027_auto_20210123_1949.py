# Generated by Django 3.1 on 2021-01-23 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0026_auto_20210120_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveorder',
            name='sessionid',
            field=models.CharField(default='0', max_length=90),
        ),
        migrations.AddField(
            model_name='order',
            name='sessionid',
            field=models.CharField(default='0', max_length=90),
        ),
        migrations.AddField(
            model_name='verifyorder',
            name='sessionid',
            field=models.CharField(default='0', max_length=90),
        ),
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 19, 49, 48, 679558)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 19, 49, 48, 679558)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 19, 49, 48, 678560)),
        ),
        migrations.AlterField(
            model_name='verifyorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 19, 49, 48, 678560)),
        ),
    ]
