# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0006_wechatmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechatmenu',
            name='slug',
            field=models.CharField(default='00', max_length=64),
        ),
    ]
