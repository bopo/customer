# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0014_auto_20161022_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='wechat_alias',
            new_name='wechat',
        ),
        migrations.RemoveField(
            model_name='member',
            name='wechat_nick',
        ),
        migrations.RemoveField(
            model_name='member',
            name='wechat_remark',
        ),
        migrations.AlterField(
            model_name='member',
            name='remark',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5fae\u4fe1\u5907\u6ce8'),
        ),
    ]
