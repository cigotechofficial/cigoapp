# Generated by Django 3.1 on 2021-02-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0010_delete_venuetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='showtype',
            field=models.BooleanField(default=1),
        ),
    ]
