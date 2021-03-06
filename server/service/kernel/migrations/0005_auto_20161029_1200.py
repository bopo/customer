# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0004_auto_20161029_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='', max_length=50, verbose_name='\u5730\u533a')),
                ('site', models.CharField(default='', max_length=50, verbose_name='\u57ce\u5e02')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kernel.Client')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u5730\u5740',
                'verbose_name_plural': '\u5ba2\u6237\u5730\u5740',
            },
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='price',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.AddField(
            model_name='orders',
            name='number',
            field=models.CharField(default='', max_length=100, verbose_name='\u8ba2\u5355\u53f7'),
        ),
    ]
