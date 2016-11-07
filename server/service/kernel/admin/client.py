# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from ..models import Address
from ..models import Client
from ..models import Goods, Category
from ..models import Groups
from ..models import Orders


class AddressAdmin(VersionAdmin):
    pass


class ClientAdmin(VersionAdmin):
    pass


class OrdersAdmin(admin.ModelAdmin):
    readonly_fields = ['number']


admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category)
admin.site.register(Groups)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Goods)
