# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0024_auto_20161107_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='openid',
            field=models.CharField(default='', max_length=100, verbose_name='openid'),
        ),
    ]
