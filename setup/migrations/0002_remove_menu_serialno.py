# Generated by Django 3.1.6 on 2021-07-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='serialno',
        ),
    ]
