# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Groups(models.Model):
    name = models.CharField(verbose_name=_(u'分组名称'), max_length=64, null=False)
    total = models.IntegerField(verbose_name=_(u'用户数'), blank=True, null=True, default=0)

    def __unicode__(self):
        return '%s (%d)' % (self.name, self.total)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'客户分组')
        verbose_name_plural = _(u'客户分组')


class Client(models.Model):
    UNITS_CHOICES = ()
    name = models.CharField(_(u'姓名'), max_length=100, default='')
    mobile = models.CharField(_(u'电话'), max_length=50, default='')
    groups = models.ForeignKey(Groups)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.mobile)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'客户列表')
        verbose_name_plural = _(u'客户列表')


class Address(models.Model):
    area = models.CharField(_(u'地区'), max_length=50, default='')
    site = models.CharField(_(u'城市'), max_length=50, default='')
    address = models.CharField(_(u'详细地址'), max_length=200, blank=True, null=True)

    client = models.ForeignKey(Client)

    def __unicode__(self):
        return '%s %s' % (self.site, self.address)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'客户地址')
        verbose_name_plural = _(u'客户地址')
