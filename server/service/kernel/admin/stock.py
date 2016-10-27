# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from ..models.stock import Stock, Basic
from ..resources.stock import StockResource


class BasicAdmin(ImportExportActionModelAdmin):
    list_display = ('code', 'name', 'area', 'industry',)
    list_filter = ('area', 'industry',)
    search_fields = ('code', 'name')


class StockAdmin(ImportExportActionModelAdmin):
    resource_class = StockResource

    list_display = ('code', 'name', 'industry', 'area', 'concept',)
    list_filter = ('area', 'industry', 'concept', 'st')


admin.site.register(Stock, StockAdmin)
admin.site.register(Basic, BasicAdmin)
