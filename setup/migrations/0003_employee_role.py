# Generated by Django 3.1 on 2020-08-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0002_employee_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
