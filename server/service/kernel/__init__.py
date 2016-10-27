# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'stock.service.RestfulConfig'


class RestfulConfig(AppConfig):
    name = 'stock.service'
    verbose_name = _(u'数据服务')
