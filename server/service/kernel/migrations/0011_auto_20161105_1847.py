# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0010_auto_20161105_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='units',
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile',
            field=models.CharField(default='', max_length=50, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]
