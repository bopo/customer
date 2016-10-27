# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20161014_1654'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.CharField(default='', max_length=100, verbose_name='\u4ee3\u7801'),
        ),
    ]
