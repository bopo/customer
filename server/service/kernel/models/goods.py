# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from pilkit.processors import ResizeToFill
from tagging.models import Tag

from . import UNITS_CHOICES

CHANNEL_CHOICES = (
    ('1000', "官网"),
    ('1001', "91助手"),
    ('1002', "百度"),
    ('1003', "安卓"),
    ('1004', "豌豆荚"),
    ('1005', "应用宝"),
    ('1006', "360"),
    ('1007', "应用汇"),
    ('1008', "魅族"),
    ('1009', "N多网"),
    ('1010', "PP助手"),
    ('1011', "淘宝"),
    ('1012', "机锋网"),
    ('1013', "金立"),
    ('1014', "小米"),
    ('1015', "华为"),
    ('1016', "搜狗"),
    ('1017', "安智"),
    ('1018', "沃商店"),
    ('1019', "itools"),
    ('1020', "电信爱游戏"),
    ('1021', "优亿市场"),
    ('1022', "应用贝"),
    ('1023', "googleplay"),
    ('1024', "安粉网")
)


class Category(MPTTModel):
    name = models.CharField(verbose_name=_(u'分类名称'), max_length=64, null=False)
    cover = models.ImageField(verbose_name=_(u'分类图片'), upload_to='category', blank=True, null=True)
    total = models.IntegerField(verbose_name=_(u'商品数'), blank=True, null=True, default=0)
    order = models.PositiveIntegerField(verbose_name=_(u'排序'), default=999, editable=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return '%s (%d)' % (self.name, self.total)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _(u'商品类别')
        verbose_name_plural = _(u'商品类别')

    class MPTTMeta:
        order_insertion_by = ['order']
        parent_attr = 'parent'


class Goods(TimeStampedModel, StatusModel):
    STATUS = Choices('draft', 'published')

    title = models.CharField(verbose_name=_(u'名称'), max_length=100, default='')
    price = models.DecimalField(verbose_name=_(u'价格'), max_digits=10, decimal_places=2, blank=True, null=True)
    units = models.CharField(verbose_name=_(u'单位'), max_length=50, choices=UNITS_CHOICES)
    order = models.IntegerField(_(u'排序'), default='1')
    summary = models.TextField(_('商品简介'), blank=True, null=True)
    cover = ProcessedImageField(verbose_name=_(u'图片'), upload_to='goods', processors=[ResizeToFill(720, 240)],
        format='JPEG', null=True, help_text=u'图片尺寸最好为720x240', blank=True)
    total = models.IntegerField(verbose_name=_('库存数'), default=0)

    # cats = models.ForeignKey(Category, blank=True, null=True)
    tags = models.CharField(verbose_name=_(u'标签关键字'), max_length=200, help_text='多个关键字之间逗号隔开')

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def update_tags(self, tag_names):
        Tag.objects.update_tags(self, tag_names)

    def remove_all_tags(self):
        Tag.objects.update_tags(self, None)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        if self.tags:
            self.tags = ',%s,' % self.tags.strip(',')

        super(Goods, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'商品列表')
        verbose_name_plural = _(u'商品列表')
