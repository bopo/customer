# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS, DEBUG

INSTALLED_APPS += (
    'service.frontend',
    'service.kernel',
    'service.wechat',
    'service.consumer',
    'service.restauth',
    'service.restauth.registration',

    'imagekit',
    'reversion',
    'easy_select2',
    'import_export',
)

CHATBOT_DEFUALT = {
    'SESSION_PATH': 'runtime/chatbot.kpl',
    'QR_CODE_PATH': 'runtime/chatbot.png',
    'DEBUG': DEBUG,
}
