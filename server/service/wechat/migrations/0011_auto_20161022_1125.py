# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0010_auto_20161018_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='wechat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u7ed1\u5b9a\u5fae\u4fe1'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='member',
            name='verify',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u9a8c\u8bc1\u7801'),
        ),
    ]