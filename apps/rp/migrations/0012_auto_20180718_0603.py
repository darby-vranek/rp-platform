# Generated by Django 2.0.7 on 2018-07-18 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rp', '0011_auto_20180714_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(max_length=255)),
                ('caption', models.CharField(blank=True, default='', max_length=255)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='charactertrait',
            old_name='char',
            new_name='character',
        ),
        migrations.RenameField(
            model_name='versetrait',
            old_name='ver',
            new_name='verse',
        ),
        migrations.RemoveField(
            model_name='biotrait',
            name='content',
        ),
        migrations.RemoveField(
            model_name='biotrait',
            name='created',
        ),
        migrations.RemoveField(
            model_name='biotrait',
            name='id',
        ),
        migrations.RemoveField(
            model_name='biotrait',
            name='title',
        ),
        migrations.RemoveField(
            model_name='biotrait',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='character',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='character',
            name='created',
        ),
        migrations.RemoveField(
            model_name='character',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='character',
            name='display_name',
        ),
        migrations.RemoveField(
            model_name='character',
            name='id',
        ),
        migrations.RemoveField(
            model_name='character',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='charactertrait',
            name='content',
        ),
        migrations.RemoveField(
            model_name='charactertrait',
            name='created',
        ),
        migrations.RemoveField(
            model_name='charactertrait',
            name='id',
        ),
        migrations.RemoveField(
            model_name='charactertrait',
            name='title',
        ),
        migrations.RemoveField(
            model_name='charactertrait',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='created',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='display_name',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='versetrait',
            name='content',
        ),
        migrations.RemoveField(
            model_name='versetrait',
            name='created',
        ),
        migrations.RemoveField(
            model_name='versetrait',
            name='id',
        ),
        migrations.RemoveField(
            model_name='versetrait',
            name='title',
        ),
        migrations.RemoveField(
            model_name='versetrait',
            name='updated',
        ),
        migrations.AddField(
            model_name='biotrait',
            name='trait_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rp.Trait'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='profile_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rp.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charactertrait',
            name='trait_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rp.Trait'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='verse',
            name='profile_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rp.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='versetrait',
            name='trait_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rp.Trait'),
            preserve_default=False,
        ),
    ]
