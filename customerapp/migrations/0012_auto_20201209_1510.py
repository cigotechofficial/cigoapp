# Generated by Django 3.1 on 2020-12-09 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0011_auto_20201209_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 15, 10, 10, 136544)),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 15, 10, 10, 136544)),
        ),
    ]
