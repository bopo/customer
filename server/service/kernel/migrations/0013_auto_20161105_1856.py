# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0012_auto_20161105_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.UUIDField(verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]