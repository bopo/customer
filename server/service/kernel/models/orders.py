# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel

from . import Goods


class Orders(TimeStampedModel, StatusModel):
    STATUS = Choices(('Created', '未付款'), ('Payment', '已付款'), ('Refund', '退款'), ('Success', '已发货'), ('Close', '交易关闭'))
    number = models.CharField(verbose_name=_(u'订单号'), max_length=200, editable=False, blank=True, null=True)
    quantity = models.IntegerField(_('数量'), default=0)
    amount = models.DecimalField(verbose_name=_(u'购物总计'), decimal_places=2, max_digits=10, blank=True, null=True)
    uin = models.CharField(verbose_name=_(u'微信标示'), max_length=100, default='', blank=True, null=True)
    nick = models.CharField(verbose_name=_('微信昵称'), max_length=200, blank=True, null=True)
    price = models.DecimalField(verbose_name=_(u'商品单价'), decimal_places=2, max_digits=10, blank=True, null=True)
    goods = models.ForeignKey(Goods, verbose_name=_('商品'))
    token = models.CharField(verbose_name=_(u'订单标示'), max_length=100, default='')
    openid = models.CharField(verbose_name=_(u'openid'), max_length=100, default='', blank=True, null=True)
    mobile = models.CharField(verbose_name=_('顾客电话'), max_length=100, blank=True, null=True)
    address = models.TextField(verbose_name=_('顾客地址'), blank=True, null=True)
    express = models.CharField(verbose_name=_('快递单号'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.goods.title

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'订单列表')
        verbose_name_plural = _(u'订单列表')
