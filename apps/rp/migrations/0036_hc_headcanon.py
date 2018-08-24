# Generated by Django 2.0.7 on 2018-08-23 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0035_auto_20180822_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Headcanon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headcanons', to='rp.Character')),
                ('hc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='headcanons', to='rp.Hc')),
                ('verse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='headcanons', to='rp.Verse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]