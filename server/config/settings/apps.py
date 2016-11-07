# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS, DEBUG

INSTALLED_APPS += (
    'service.frontend',
    'service.kernel',
    # 'service.wechat',
    'service.consumer',
    'service.restauth',
    'service.restauth.registration',

    'tagging',
    'imagekit',
    'reversion',
    'easy_select2',
    'import_export',
    'django_extensions',
)

CHATBOT_DEFUALT = {
    'SESSION_PATH': 'runtime/chatbot.kpl',
    'QR_CODE_PATH': 'runtime/chatbot.png',
    'DEBUG': DEBUG,
}

TOP_APPKEY = '23255563'
TOP_SECRET = 'f7092fdb96f20625742d577820936b5c'
