# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0002_auto_20161017_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created',
                model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created',
                    editable=False)),
                ('modified',
                model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified',
                    editable=False)),
                ('nick',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u6635\u79f0', blank=True)),
                ('name',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u59d3\u540d', blank=True)),
                ('mobile',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u624b\u673a', blank=True)),
                ('verify',
                models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u6d88\u606f',
                    max_length=50, verbose_name='\u9a8c\u8bc1\u7801', blank=True)),
                ('avatar', models.ImageField(upload_to=b'', verbose_name='\u5934\u50cf')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u4f1a\u5458',
                'verbose_name_plural': '\u5fae\u4fe1\u4f1a\u5458',
            },
        ),
        migrations.AlterField(
            model_name='patterne2pt',
            name='event',
            field=models.CharField(default='CLICK', max_length=30, verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
                choices=[('subscribe', '\u5173\u6ce8\u4e8b\u4ef6'),
                    ('unsubscribe', '\u53d6\u6d88\u5173\u6ce8\u4e8b\u4ef6'), ('SCAN', '\u626b\u63cf\u4e8c\u7ef4\u7801'),
                    ('LOCATION', '\u4e0a\u62a5\u5730\u7406\u4f4d\u7f6e'),
                    ('CLICK', '\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6'),
                    ('VIEW', '\u7528\u6237\u70b9\u51fb\u94fe\u63a5\u7684\u8df3\u8f6c\u4e8b\u4ef6')]),
        ),
        migrations.AlterField(
            model_name='patterne2pt',
            name='event_key',
            field=models.CharField(
                help_text='<strong>\u5bf9\u4e8e\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6\u548c\u81ea\u5b9a\u4e49\u94fe\u63a5\u8df3\u8f6c\u4e8b\u4ef6\u8fd9\u4e2a\u662f\u5fc5\u586b\u7684\uff01</strong>',
                max_length=255, verbose_name='event_key\u6216\u8005\u81ea\u5b9a\u4e49url', blank=True),
        ),
        migrations.AlterField(
            model_name='patterne2pt',
            name='type',
            field=models.CharField(default='event',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[('text', '\u6587\u672c\u6d88\u606f'), ('event', '\u4e8b\u4ef6\u6d88\u606f'),
                    ('image', '\u56fe\u7247\u6d88\u606f'), ('location', '\u4f4d\u7f6e\u6d88\u606f'),
                    ('voice', '\u8bed\u97f3\u6d88\u606f'), ('video', '\u89c6\u9891\u6d88\u606f')]),
        ),
        migrations.AlterField(
            model_name='patterne2t',
            name='event',
            field=models.CharField(default='CLICK',
                help_text='\u9664\u975e\u6536\u5230\u7684\u6d88\u606f\u7c7b\u578b\u4e3a\u201c\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6\u6216\u8005\u70b9\u51fb\u94fe\u63a5\u8df3\u8f6c\u4e8b\u4ef6\uff0c\u5426\u5219\u4e0d\u8981\u4fee\u6539\u672c\u5b57\u6bb5\u201d',
                max_length=30, verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
                choices=[('subscribe', '\u5173\u6ce8\u4e8b\u4ef6'),
                    ('unsubscribe', '\u53d6\u6d88\u5173\u6ce8\u4e8b\u4ef6'), ('SCAN', '\u626b\u63cf\u4e8c\u7ef4\u7801'),
                    ('LOCATION', '\u4e0a\u62a5\u5730\u7406\u4f4d\u7f6e'),
                    ('CLICK', '\u81ea\u5b9a\u4e49\u83dc\u5355\u4e8b\u4ef6'),
                    ('VIEW', '\u7528\u6237\u70b9\u51fb\u94fe\u63a5\u7684\u8df3\u8f6c\u4e8b\u4ef6')]),
        ),
        migrations.AlterField(
            model_name='patterne2t',
            name='type',
            field=models.CharField(default='event', max_length=20,
                verbose_name='\u6536\u5230\u7684\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[('text', '\u6587\u672c\u6d88\u606f'), ('event', '\u4e8b\u4ef6\u6d88\u606f'),
                    ('image', '\u56fe\u7247\u6d88\u606f'), ('location', '\u4f4d\u7f6e\u6d88\u606f'),
                    ('voice', '\u8bed\u97f3\u6d88\u606f'), ('video', '\u89c6\u9891\u6d88\u606f')]),
        ),
        migrations.AlterField(
            model_name='patternt2pt',
            name='type',
            field=models.CharField(default='text',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[('text', '\u6587\u672c\u6d88\u606f'), ('event', '\u4e8b\u4ef6\u6d88\u606f'),
                    ('image', '\u56fe\u7247\u6d88\u606f'), ('location', '\u4f4d\u7f6e\u6d88\u606f'),
                    ('voice', '\u8bed\u97f3\u6d88\u606f'), ('video', '\u89c6\u9891\u6d88\u606f')]),
        ),
        migrations.AlterField(
            model_name='patternt2t',
            name='name',
            field=models.CharField(help_text='\u53ef\u4ee5\u4e3a\u7a7a\uff0c\u4ec5\u7528\u6765\u6807\u8bc6\u89c4\u5219',
                max_length=50, verbose_name='\u89c4\u5219\u547d\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='patternt2t',
            name='type',
            field=models.CharField(default='text',
                help_text='\u9664\u975e\u4f60\u6e05\u695a\u8fd9\u4e2a\u5b57\u6bb5\u7684\u542b\u4e49\uff0c\u5426\u5219\u8bf7\u4e0d\u8981\u968f\u610f\u66f4\u6539',
                max_length=20, verbose_name='\u7528\u6237\u6d88\u606f\u7c7b\u578b(\u8bf7\u4fdd\u6301\u9ed8\u8ba4)',
                choices=[('text', '\u6587\u672c\u6d88\u606f'), ('event', '\u4e8b\u4ef6\u6d88\u606f'),
                    ('image', '\u56fe\u7247\u6d88\u606f'), ('location', '\u4f4d\u7f6e\u6d88\u606f'),
                    ('voice', '\u8bed\u97f3\u6d88\u606f'), ('video', '\u89c6\u9891\u6d88\u606f')]),
        ),
    ]
