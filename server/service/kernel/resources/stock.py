# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export.resources import ModelResource

from ..models.stock import Stock


class StockResource(ModelResource):
    class Meta:
        model = Stock
        # exclude = ('id',)
        # fields = ('id', 'name', 'author', 'price',)
        # export_order = ('id', 'price', 'author', 'name')
        # import_id_fields = ('isbn',)
        # fields = ('author__name',) 外键
        # skip_unchanged = True
        # report_skipped = False
