# Generated by Django 3.1 on 2021-02-09 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0036_auto_20210209_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 44, 23, 336900)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 44, 23, 336900)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 44, 23, 334905)),
        ),
        migrations.AlterField(
            model_name='verifyorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 20, 44, 23, 335903)),
        ),
    ]
