# Generated by Django 2.1.5 on 2020-09-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200913_2152'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DSComment',
        ),
        
        migrations.AddField(
            model_name='comment',
            name='addid',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
