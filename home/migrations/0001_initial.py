# Generated by Django 3.1.6 on 2021-06-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Defaultimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Gst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cgst', models.DecimalField(decimal_places=1, max_digits=6)),
                ('sgst', models.DecimalField(decimal_places=1, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Newuserinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
