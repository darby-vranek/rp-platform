# Generated by Django 2.0.7 on 2018-07-25 04:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0024_auto_20180725_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to='images'),
        ),
    ]
