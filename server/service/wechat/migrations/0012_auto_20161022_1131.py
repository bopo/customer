# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0011_auto_20161022_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
    ]
