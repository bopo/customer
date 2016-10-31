# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wechat', '0007_wechatmenu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbimgtextmsg',
            name='description',
            field=models.TextField(verbose_name='\u6d88\u606f\u63cf\u8ff0', blank=True),
        ),
    ]
