# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20161016_0019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u91c7\u96c6\u6587\u7ae0', 'verbose_name_plural': '\u91c7\u96c6\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='newswebsite',
            options={'verbose_name': '\u91c7\u96c6\u7ad9\u70b9', 'verbose_name_plural': '\u91c7\u96c6\u7ad9\u70b9'},
        ),
        migrations.AddField(
            model_name='article',
            name='stock',
            field=models.ForeignKey(default=0, verbose_name='\u76f8\u5173\u80a1\u7968', to='service.Stock'),
            preserve_default=False,
        ),
    ]
