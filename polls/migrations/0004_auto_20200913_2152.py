# Generated by Django 2.1.5 on 2020-09-14 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='DSComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='cId',
            fields=[
                ('name', models.CharField(max_length=12)),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
            ],
        ),  
    ]
