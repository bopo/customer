# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from reversion.admin import VersionAdmin

from service.kernel.resources.goods import OrdersResource
from ..models import Address
from ..models import Client
from ..models import Goods, Category
from ..models import Groups
from ..models import Orders


class AddressAdmin(VersionAdmin):
    pass


class ClientAdmin(VersionAdmin):
    pass


# STATUS = Choices('pay_success', )
# number = models.CharField(verbose_name=_(u'订单号'), max_length=200, editable=False, blank=True, null=True)
# quantity = models.IntegerField(_('数量'), default=0)
# # expired = models.DateTimeField(verbose_name=_(u'过期时间'), default='')
# amount = models.DecimalField(verbose_name=_(u'购物总计'), decimal_places=2, max_digits=10, blank=True, null=True)
# price = models.DecimalField(verbose_name=_(u'商品单价'), decimal_places=2, max_digits=10, blank=True, null=True)
# goods = models.ForeignKey(Goods)
# uin = models.CharField(verbose_name=_(u'商品数量'), max_length=100, default='')
# token = models.CharField(verbose_name=_(u'订单标示'), max_length=100, default='')
# openid = models.CharField(verbose_name=_(u'openid'), max_length=100, default='')

# class GoodsAdmin(VersionAdmin, ImportExportModelAdmin):
@admin.register(Orders)
class OrdersAdmin(VersionAdmin, ExportActionModelAdmin):
    resource_class = OrdersResource

    def price_(self, obj):
        return obj.goods.price

    list_display = ('goods', 'price_', 'quantity', 'amount', 'nick', 'status', 'express', 'created')
    readonly_fields = ['number']
    list_editable = ('status', 'express')
    list_filter = ('status',)
    search_fields = ('nick',)


admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category)
admin.site.register(Groups)


# admin.site.register(Orders, OrdersAdmin)


class GoodsAdmin(VersionAdmin):
    list_display = ('title', 'price', 'total')


admin.site.register(Goods, GoodsAdmin)

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'template_name')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                # 'enable_comments',
                # 'registration_required',
                # 'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
