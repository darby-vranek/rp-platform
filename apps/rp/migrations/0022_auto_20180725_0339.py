# Generated by Django 2.0.7 on 2018-07-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0021_auto_20180725_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='fc',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]