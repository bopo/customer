# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0003_auto_20161017_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='WechatMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u540d\u79f0', blank=True)),
                ('type',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u7c7b\u578b', blank=True)),
                ('key',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u952e\u503c', blank=True)),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u83dc\u5355',
                'verbose_name_plural': '\u5fae\u4fe1\u83dc\u5355',
            },
        ),
    ]
