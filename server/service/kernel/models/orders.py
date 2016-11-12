# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel

from . import Goods


class Orders(TimeStampedModel, StatusModel):
    STATUS = Choices('pay_success', )
    number = models.CharField(verbose_name=_(u'订单号'), max_length=200, editable=False, blank=True, null=True)
    quantity = models.IntegerField(_('数量'), default=0)
    # expired = models.DateTimeField(verbose_name=_(u'过期时间'), default='')
    amount = models.DecimalField(verbose_name=_(u'购物总计'), decimal_places=2, max_digits=10, blank=True, null=True)
    price = models.DecimalField(verbose_name=_(u'商品单价'), decimal_places=2, max_digits=10, blank=True, null=True)
    goods = models.ForeignKey(Goods)
    uin = models.CharField(verbose_name=_(u'商品数量'), max_length=100, default='')
    token = models.CharField(verbose_name=_(u'订单标示'), max_length=100, default='')
    openid = models.CharField(verbose_name=_(u'openid'), max_length=100, default='')

    def __unicode__(self):
        return self.goods.title

    def __str__(self):
        return self.__unicode__()

    # def save(self, *args, **kwargs):
    #     self.number = uuid.uuid1().hex
    #     super(Orders, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'订单列表')
        verbose_name_plural = _(u'订单列表')
