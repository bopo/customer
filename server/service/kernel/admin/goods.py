# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models import Orders
from ..models import Category
from ..models import Goods


class OrdersAdmin(VersionAdmin):
    pass


class CategoryAdmin(VersionAdmin):
    pass


class GoodsAdmin(VersionAdmin):
    # list_display = ('name', 'price', 'status', 'created',)

    # def has_add_permission(self, request):
    #     pass

    def make_rejected(self, request, queryset):
        rows_updated = queryset.update(status='rejected')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='success')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    make_rejected.short_description = u"驳回选中的提现"
    make_published.short_description = u"完成选中的提现"

    # actions = [make_rejected, make_published]


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Orders, OrdersAdmin)
