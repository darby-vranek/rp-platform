# Generated by Django 2.0.7 on 2018-08-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0033_auto_20180808_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='short_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=35),
        ),
    ]
