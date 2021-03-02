# Generated by Django 3.1 on 2020-09-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
        migrations.AddField(
            model_name='menu',
            name='product_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
