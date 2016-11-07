# -*- coding: utf-8 -*-
default_app_config = 'service.kernel.KernelConfig'
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class KernelConfig(AppConfig):
    name = 'service.kernel'
    verbose_name = _(u'商业数据')
