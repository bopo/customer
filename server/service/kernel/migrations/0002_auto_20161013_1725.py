# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': '\u80a1\u7968\u6570\u636e', 'verbose_name_plural': '\u80a1\u7968\u6570\u636e'},
        ),
        migrations.RemoveField(
            model_name='stock',
            name='board',
        ),
    ]
