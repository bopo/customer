# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0029_auto_20161112_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='total',
            field=models.IntegerField(default=0, verbose_name='\u5e93\u5b58\u6570'),
        ),
    ]