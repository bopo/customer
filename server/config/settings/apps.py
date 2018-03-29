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


# JPUSH_APPKEY = u'5432833aa78e771efca25be3'
# JPUSH_SECRET = u'0ed88cbd56b67e96a9df7885'

# WECHAT_APPKEY = 'wx25cb974381f02fa1'
# WECHAT_SECRET = 'fe59d7ab30c2a96ebd086c4d09a1746f'

WECHAT_APPKEY = 'wx25cb974381f02fa1'
WECHAT_SECRET = 'fe59d7ab30c2a96ebd086c4d09a1746f'

# WECHAT_APPKEY = 'wx95d4b735c05ff6a7'
# WECHAT_SECRET = '5c330e437a2ebf13faf122551b103520'
