# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBImgTextMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u6d88\u606f\u540d\u79f0', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u6d88\u606f\u6807\u9898', blank=True)),
                ('description', models.CharField(max_length=255, verbose_name='\u6d88\u606f\u63cf\u8ff0', blank=True)),
                ('pic_url', models.URLField(verbose_name='\u56fe\u7247\u5730\u5740')),
                ('url', models.URLField(max_length=255, verbose_name='\u6587\u7ae0\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u7ba1\u7406(\u56fe\u6587\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u7ba1\u7406(\u56fe\u6587\u6d88\u606f)',
            },
        ),
        migrations.CreateModel(
            name='DBTextMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u6d88\u606f\u540d\u5b57', blank=True)),
                ('content', models.TextField(verbose_name='\u6d88\u606f\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u7ba1\u7406(\u6587\u5b57\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u7ba1\u7406(\u6587\u5b57\u6d88\u606f)',
            },
        ),
        migrations.CreateModel(
            name='PatternE2PT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u89c4\u5219',
                    max_length=50, verbose_name='\u89c4\u5219\u547d\u540d', blank=True)),
                ('type', models.CharField(default=b'event',
                    help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                    max_length=20,
                    verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b\uff08\u8bf7\u4fdd\u6301\u9ed8\u8ba4\uff09',
                    choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')])),
                ('event', models.CharField(default=b'CLICK', max_length=30, verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
                    choices=[(b'subscribe', b'\xe5\x85\xb3\xe6\xb3\xa8\xe4\xba\x8b\xe4\xbb\xb6'),
                        (b'unsubscribe', b'\xe5\x8f\x96\xe6\xb6\x88\xe5\x85\xb3\xe6\xb3\xa8\xe4\xba\x8b\xe4\xbb\xb6'),
                        (b'SCAN', b'\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81'),
                        (b'LOCATION', b'\xe4\xb8\x8a\xe6\x8a\xa5\xe5\x9c\xb0\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae'), (
                        b'CLICK',
                        b'\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x8f\x9c\xe5\x8d\x95\xe4\xba\x8b\xe4\xbb\xb6'), (
                        b'VIEW',
                        b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x82\xb9\xe5\x87\xbb\xe9\x93\xbe\xe6\x8e\xa5\xe7\x9a\x84\xe8\xb7\xb3\xe8\xbd\xac\xe4\xba\x8b\xe4\xbb\xb6')])),
                ('event_key', models.CharField(
                    help_text=b'<strong>\xe5\xaf\xb9\xe4\xba\x8e\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x8f\x9c\xe5\x8d\x95\xe4\xba\x8b\xe4\xbb\xb6\xe5\x92\x8c\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe9\x93\xbe\xe6\x8e\xa5\xe8\xb7\xb3\xe8\xbd\xac\xe4\xba\x8b\xe4\xbb\xb6\xe8\xbf\x99\xe4\xb8\xaa\xe6\x98\xaf\xe5\xbf\x85\xe5\xa1\xab\xe7\x9a\x84\xef\xbc\x81</strong>',
                    max_length=255, verbose_name='event_key\u6216\u8005\u81ea\u5b9a\u4e49url', blank=True)),
                ('handler', models.ManyToManyField(
                    help_text='\u6700\u591a\u5141\u8bb8\u4e94\u6761\uff0c\u4e0d\u7136\u4f1a\u51fa\u9519',
                    to='wechat.DBImgTextMsg', verbose_name='\u56de\u590d\u6d88\u606f')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u89c4\u5219\u7ba1\u7406\uff08\u4e8b\u4ef6>\u56fe\u6587\u6d88\u606f\u56de\u590d\uff09',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219\u7ba1\u7406\uff08\u4e8b\u4ef6>\u56fe\u6587\u6d88\u606f\u56de\u590d\uff09',
            },
        ),
        migrations.CreateModel(
            name='PatternE2T',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u89c4\u5219',
                    max_length=50, verbose_name='\u89c4\u5219\u547d\u540d', blank=True)),
                ('type', models.CharField(default=b'event', max_length=20,
                    verbose_name='\u6536\u5230\u7684\u6d88\u606f\u7c7b\u578b\uff08\u8bf7\u4fdd\u6301\u9ed8\u8ba4\uff09',
                    choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')])),
                ('event', models.CharField(default=b'CLICK',
                    help_text='\u9664\u975e\u6536\u5230\u7684\u6d88\u606f\u7c7b\u578b\u4e3a\u201c\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6\u6216\u8005\u70b9\u51fb\u94fe\u63a5\u8df3\u8f6c\u4e8b\u4ef6\uff0c\u5426\u5219\u4e0d\u8981\u4fee\u6539\u672c\u5b57\u6bb5\u201d',
                    max_length=30, verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
                    choices=[(b'subscribe', b'\xe5\x85\xb3\xe6\xb3\xa8\xe4\xba\x8b\xe4\xbb\xb6'),
                        (b'unsubscribe', b'\xe5\x8f\x96\xe6\xb6\x88\xe5\x85\xb3\xe6\xb3\xa8\xe4\xba\x8b\xe4\xbb\xb6'),
                        (b'SCAN', b'\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81'),
                        (b'LOCATION', b'\xe4\xb8\x8a\xe6\x8a\xa5\xe5\x9c\xb0\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae'), (
                        b'CLICK',
                        b'\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x8f\x9c\xe5\x8d\x95\xe4\xba\x8b\xe4\xbb\xb6'), (
                        b'VIEW',
                        b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x82\xb9\xe5\x87\xbb\xe9\x93\xbe\xe6\x8e\xa5\xe7\x9a\x84\xe8\xb7\xb3\xe8\xbd\xac\xe4\xba\x8b\xe4\xbb\xb6')])),
                ('event_key', models.CharField(
                    help_text='<strong>\u5bf9\u4e8e\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6\u548c\u81ea\u5b9a\u4e49\u94fe\u63a5\u8df3\u8f6c\u4e8b\u4ef6\u8fd9\u4e2a\u662f\u5fc5\u586b\u7684\uff01</strong>',
                    max_length=255, verbose_name='event_key\u6216\u8005\u81ea\u5b9a\u4e49url', blank=True)),
                ('handler', models.ForeignKey(verbose_name='\u56de\u590d\u6d88\u606f', to='wechat.DBTextMsg')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u4e8b\u4ef6>\u6587\u672c\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u4e8b\u4ef6>\u6587\u672c\u6d88\u606f)',
            },
        ),
        migrations.CreateModel(
            name='PatternT2PT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u89c4\u5219',
                    max_length=50, verbose_name='\u89c4\u5219\u547d\u540d', blank=True)),
                ('type', models.CharField(default=b'text',
                    help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                    max_length=20,
                    verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b\uff08\u8bf7\u4fdd\u6301\u9ed8\u8ba4\uff09',
                    choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')])),
                ('content', models.CharField(help_text='\u4f7f\u7528\u6b63\u5219\u8868\u8fbe\u5f0f', max_length=50,
                    verbose_name='\u9700\u8981\u5339\u914d\u7684\u6d88\u606f', blank=True)),
                ('handler', models.ManyToManyField(
                    help_text='\u6700\u591a\u5141\u8bb8\u4e94\u6761\uff0c\u4e0d\u7136\u4f1a\u51fa\u9519',
                    to='wechat.DBImgTextMsg', verbose_name='\u56de\u590d\u6d88\u606f')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u6587\u672c>\u56fe\u6587\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u6587\u672c>\u56fe\u6587\u6d88\u606f)',
            },
        ),
        migrations.CreateModel(
            name='PatternT2T',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u89c4\u5219',
                    max_length=50, verbose_name=b'\xe8\xa7\x84\xe5\x88\x99\xe5\x91\xbd\xe5\x90\x8d', blank=True)),
                ('type', models.CharField(default=b'text',
                    help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                    max_length=20,
                    verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b\uff08\u8bf7\u4fdd\u6301\u9ed8\u8ba4\uff09',
                    choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                        (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')])),
                ('content', models.CharField(help_text='\u4f7f\u7528\u6b63\u5219\u8868\u8fbe\u5f0f', max_length=100,
                    verbose_name='\u6536\u5230\u7684\u6d88\u606f', blank=True)),
                ('handler',
                models.ForeignKey(verbose_name='\u54cd\u5e94\u7684\u6d88\u606f\u5185\u5bb9', to='wechat.DBTextMsg')),
            ],
            options={
                'verbose_name': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u6587\u672c>\u6587\u672c\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219\u7ba1\u7406(\u6587\u672c>\u6587\u672c\u6d88\u606f)',
            },
        ),
    ]
