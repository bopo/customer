# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0019_auto_20161105_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='\u6570\u91cf'),
        ),
    ]
