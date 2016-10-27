# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

class Term(models.Model):
    keyword = models.CharField(verbose_name=_(u'名词'), max_length=100, default='')
    content = models.TextField(verbose_name=_(u'解释'), default='')

    class Meta:
        verbose_name = _(u'名词解释')
        verbose_name_plural = _(u'名词解释')

    def __unicode__(self):
        return self.keyword

    def __str__(self):
        return self.__unicode__()

class Basic(models.Model):
    '''
    '''
    code = models.CharField(verbose_name=_(u'代码'), max_length=100, default='', unique=True)
    name = models.CharField(verbose_name=_(u'名称'), max_length=100, default='')
    area = models.CharField(verbose_name=_('所在地区'), max_length=100, default='')
    industry = models.CharField(verbose_name=_('所属行业'), max_length=100, default='')
    pe = models.CharField(verbose_name=_('市盈率'), max_length=100, default='')
    outstanding = models.CharField(verbose_name=_('流通股本'), max_length=100, default='')
    totals = models.CharField(verbose_name=_('总股本(万)'), max_length=100, default='')
    totalAssets = models.CharField(verbose_name=_('总资产(万)'), max_length=100, default='')
    liquidAssets = models.CharField(verbose_name=_('流动资产'), max_length=100, default='')
    fixedAssets = models.CharField(verbose_name=_('固定资产'), max_length=100, default='')

    reserved = models.CharField(verbose_name=_('公积金'), max_length=100, default='')
    reservedPerShare = models.CharField(verbose_name=_('每股公积金'), max_length=100, default='')
    eps = models.CharField(verbose_name=_('每股收益'), max_length=100, default='')
    bvps = models.CharField(verbose_name=_('每股净资'), max_length=100, default='')
    pb = models.CharField(verbose_name=_('市净率'), max_length=100, default='')
    timeToMarket = models.CharField(verbose_name=_('上市日期'), max_length=100, default='')


    class Meta:
        verbose_name = _(u'股票基本面')
        verbose_name_plural = _(u'股票基本面')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class Stock(models.Model):
    '''
    股票模型
    '''
    name = models.CharField(verbose_name=_(u'名称'), max_length=100, default='')
    logo = ProcessedImageField(verbose_name=_(u'图标'), upload_to='logo', processors=[ResizeToFill(720, 240)],
        format='JPEG', null=True, help_text=u'图片尺寸最好为720x240')
    code = models.CharField(verbose_name=_(u'代码'), max_length=100, default='')
    area = models.CharField(verbose_name=_('地域'), max_length=100, default='')
    industry = models.CharField(verbose_name=_('行业'), max_length=100, default='')
    concept = models.CharField(verbose_name=_('概念'), max_length=100, default='')
    sem = models.BooleanField(verbose_name=_('中小板'), default=False)
    gem = models.BooleanField(verbose_name=_('创业板'), default=False)
    st = models.BooleanField(verbose_name=_('风险警示板*ST'), default=False)
    hs300s = models.BooleanField(verbose_name=_('沪深300成份及权重'), default=False)
    sz50s = models.BooleanField(verbose_name=_('上证50成份股'), default=False)
    zz500s = models.BooleanField(verbose_name=_('中证500成份股'), default=False)
    terminated = models.BooleanField(verbose_name=_('终止上市'), default=False)
    suspended = models.BooleanField(verbose_name=_('暂停上市'), default=False)

    class Meta:
        verbose_name = _(u'股票数据')
        verbose_name_plural = _(u'股票数据')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
