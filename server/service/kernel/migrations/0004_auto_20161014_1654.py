# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20161013_1749'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='cover',
            new_name='logo',
        ),
        migrations.AddField(
            model_name='stock',
            name='area',
            field=models.CharField(default='', max_length=100, verbose_name='\u5730\u57df'),
        ),
        migrations.AddField(
            model_name='stock',
            name='concept',
            field=models.CharField(default='', max_length=100, verbose_name='\u6982\u5ff5'),
        ),
        migrations.AddField(
            model_name='stock',
            name='gem',
            field=models.BooleanField(default=False, verbose_name='\u521b\u4e1a\u677f'),
        ),
        migrations.AddField(
            model_name='stock',
            name='hs300s',
            field=models.BooleanField(default=False, verbose_name='\u6caa\u6df1300\u6210\u4efd\u53ca\u6743\u91cd'),
        ),
        migrations.AddField(
            model_name='stock',
            name='industry',
            field=models.CharField(default='', max_length=100, verbose_name='\u884c\u4e1a'),
        ),
        migrations.AddField(
            model_name='stock',
            name='sem',
            field=models.BooleanField(default=False, verbose_name='\u4e2d\u5c0f\u677f'),
        ),
        migrations.AddField(
            model_name='stock',
            name='st',
            field=models.BooleanField(default=False, verbose_name='\u98ce\u9669\u8b66\u793a\u677f*ST'),
        ),
        migrations.AddField(
            model_name='stock',
            name='suspended',
            field=models.BooleanField(default=False, verbose_name='\u6682\u505c\u4e0a\u5e02'),
        ),
        migrations.AddField(
            model_name='stock',
            name='sz50s',
            field=models.BooleanField(default=False, verbose_name='\u4e0a\u8bc150\u6210\u4efd\u80a1'),
        ),
        migrations.AddField(
            model_name='stock',
            name='terminated',
            field=models.BooleanField(default=False, verbose_name='\u7ec8\u6b62\u4e0a\u5e02'),
        ),
        migrations.AddField(
            model_name='stock',
            name='zz500s',
            field=models.BooleanField(default=False, verbose_name='\u4e2d\u8bc1500\u6210\u4efd\u80a1'),
        ),
    ]
