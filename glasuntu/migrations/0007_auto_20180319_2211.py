# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasuntu', '0006_auto_20180319_2035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Gig',
        ),
        migrations.AddField(
            model_name='artistpage',
            name='genre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='artistpage',
            name='info',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='artistpage',
            name='picture',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='artistpage',
            name='website',
            field=models.CharField(default='', max_length=200),
        ),
    ]
