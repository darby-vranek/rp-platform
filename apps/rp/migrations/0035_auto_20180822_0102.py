# Generated by Django 2.0.7 on 2018-08-22 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0034_auto_20180822_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
