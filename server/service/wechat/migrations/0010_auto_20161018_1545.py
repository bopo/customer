# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0009_member_openid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='nick',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=50, verbose_name='\u57ce\u5e02', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='country',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=50, verbose_name='\u56fd\u5bb6', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='groupid',
            field=models.IntegerField(null=True, verbose_name='\u5206\u7ec4ID', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='headimgurl',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=200, verbose_name='\u5934\u50cf', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='language',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=50, verbose_name='\u8bed\u8a00', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='province',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=50, verbose_name='\u7701\u4efd', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='remark',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=200, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='sex',
            field=models.SmallIntegerField(null=True, verbose_name='\u6027\u522b', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='subscribe_time',
            field=models.BigIntegerField(null=True, verbose_name='\u5173\u6ce8\u4e8b\u4ef6', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='unionid',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                max_length=200, verbose_name='\u552f\u4e00\u6807\u793a', blank=True),
        ),
    ]
