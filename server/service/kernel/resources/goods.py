# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export import resources

from service.kernel.models import Goods
from service.kernel.models import Orders


class GoodsResource(resources.ModelResource):
    class Meta:
        model = Goods
        exclude = ('tags',)
        # fields = ('id', 'name', 'author', 'price',)
        # export_order = ('id', 'price', 'author', 'name')
        # import_id_fields = ('isbn',)
        # fields = ('author__name',) 外键
        # skip_unchanged = True
        # report_skipped = False


class OrdersResource(resources.ModelResource):
    class Meta:
        model = Orders
        exclude = ('tags',)
