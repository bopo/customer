# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=100, verbose_name='\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u80a1\u7968\u677f\u5757',
                'verbose_name_plural': '\u80a1\u7968\u677f\u5757',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.TextField(default='', max_length=100, verbose_name='\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u80a1\u7968\u677f\u5757',
                'verbose_name_plural': '\u80a1\u7968\u677f\u5757',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=100, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(default='', max_length=100, verbose_name='\u53f7\u7801')),
                ('cover', imagekit.models.fields.ProcessedImageField(help_text='\u56fe\u7247\u5c3a\u5bf8\u6700\u597d\u4e3a720x240', upload_to='logo', null=True, verbose_name='\u56fe\u6807')),
                ('board', models.ForeignKey(default='', verbose_name='\u677f\u5757', to='service.Board')),
            ],
            options={
                'verbose_name': '\u80a1\u7968\u4e66\u7c4d',
                'verbose_name_plural': '\u80a1\u7968\u4e66\u7c4d',
            },
        ),
    ]
