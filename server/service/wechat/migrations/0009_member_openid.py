# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0008_auto_20161018_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='openid',
            field=models.CharField(help_text='\u4e0d\u80fd\u4e3a\u7a7a', unique=True, max_length=50,
                verbose_name='openid', blank=True),
        ),
    ]
