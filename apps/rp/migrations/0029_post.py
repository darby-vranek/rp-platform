# Generated by Django 2.0.7 on 2018-07-30 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0028_auto_20180725_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='Untitled', max_length=255)),
                ('content', models.TextField(default='')),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='rp.Character')),
                ('verse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='rp.Verse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
