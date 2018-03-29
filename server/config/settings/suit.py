# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS = ("suit",) + INSTALLED_APPS + (
    # 'suit_redactor', 
    'mptt',
)

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'微商管理平台',
    # 'HEADER_DATE_FORMAT': 'Y-m-d H:i',
    'HEADER_TIME_FORMAT': 'Y-m-d H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    # 'MENU_OPEN_FIRST_CHILD': True,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        # 'sites',
        # {'app': '认证', 'icon': 'icon-lock', 'models': ('user', 'group')},
        # {'label': '商业管理', 'icon': 'icon-cog', 'models': ('kernel.orders', 'kernel.goods')},
        {'label': '商业管理', 'icon': 'icon-cog', 'models': ('kernel.orders', 'kernel.goods', 'flatpage.flatpage')},
        {'label': '相关设置', 'icon': 'icon-cog', 'url': '/admin/flatpages/flatpage/'},
        # {'label': '设置', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
        # {'label': '支持', 'icon': 'icon-question-sign', 'url': '/admin/doc/'},
    ),
    # ),

    # misc
    'LIST_PER_PAGE': 15,
}
