# Generated by Django 3.1.6 on 2021-06-14 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverycustomerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivedeliveryorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 20, 44, 47, 336665)),
        ),
        migrations.AlterField(
            model_name='deliveryorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 20, 44, 47, 336665)),
        ),
    ]
