# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_basic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='code',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='\u4ee3\u7801'),
        ),
    ]
