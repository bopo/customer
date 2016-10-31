# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patterne2pt',
            options={'verbose_name': '\u56de\u590d\u89c4\u5219(\u4e8b\u4ef6>\u56fe\u6587\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219(\u4e8b\u4ef6>\u56fe\u6587\u6d88\u606f)'},
        ),
        migrations.AlterModelOptions(
            name='patterne2t',
            options={'verbose_name': '\u56de\u590d\u89c4\u5219(\u4e8b\u4ef6>\u6587\u672c\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219(\u4e8b\u4ef6>\u6587\u672c\u6d88\u606f)'},
        ),
        migrations.AlterModelOptions(
            name='patternt2pt',
            options={'verbose_name': '\u56de\u590d\u89c4\u5219(\u6587\u672c>\u56fe\u6587\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219(\u6587\u672c>\u56fe\u6587\u6d88\u606f)'},
        ),
        migrations.AlterModelOptions(
            name='patternt2t',
            options={'verbose_name': '\u56de\u590d\u89c4\u5219(\u6587\u672c>\u6587\u672c\u6d88\u606f)',
                'verbose_name_plural': '\u56de\u590d\u89c4\u5219(\u6587\u672c>\u6587\u672c\u6d88\u606f)'},
        ),
        migrations.AlterField(
            model_name='patterne2pt',
            name='type',
            field=models.CharField(default=b'event',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')]),
        ),
        migrations.AlterField(
            model_name='patterne2t',
            name='type',
            field=models.CharField(default=b'event', max_length=20,
                verbose_name='\u6536\u5230\u7684\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')]),
        ),
        migrations.AlterField(
            model_name='patternt2pt',
            name='type',
            field=models.CharField(default=b'text',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')]),
        ),
        migrations.AlterField(
            model_name='patternt2t',
            name='type',
            field=models.CharField(default=b'text',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[(b'text', b'\xe6\x96\x87\xe6\x9c\xac\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'event', b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'image', b'\xe5\x9b\xbe\xe7\x89\x87\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'location', b'\xe4\xbd\x8d\xe7\xbd\xae\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'voice', b'\xe8\xaf\xad\xe9\x9f\xb3\xe6\xb6\x88\xe6\x81\xaf'),
                    (b'video', b'\xe8\xa7\x86\xe9\xa2\x91\xe6\xb6\x88\xe6\x81\xaf')]),
        ),
    ]
