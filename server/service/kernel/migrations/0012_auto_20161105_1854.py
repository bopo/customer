# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0011_auto_20161105_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.CharField(default='uuid.uuid1()', max_length=200, verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]