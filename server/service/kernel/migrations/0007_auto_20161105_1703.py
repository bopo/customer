# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0006_auto_20161105_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='\u5546\u54c1\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='\u5206\u7c7b\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='units',
            field=models.CharField(choices=[('\u76d2', '\u76d2'), ('\u7bb1', '\u7bb1'), ('\u5957', '\u5957'), ('\u4e2a', '\u4e2a')], max_length=50, verbose_name='\u5355\u4f4d'),
        ),
    ]
