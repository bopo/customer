# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from wechatpy import WeChatClient

from service.kernel.models import Goods


def handler(message, *args, **kwargs):
    queryset = Goods.objects.filter(title__isnull=False)
    results = queryset.all()

    if not results:
        return None

    message = '''
===================
'''
    quantity = 1

    for result in results:
        url = 'http://ws.gjingxi.com/buy/?id=%d&q=%d&uin=%s&nick=%s' % (int(result.id), int(quantity), uin, nick)
        client = WeChatClient(settings.WECHAT_APPKEY, settings.WECHAT_SECRET)
        short_url = client.misc.short_url(long_url=url)['short_url']

        amount = float(float(result.price) * float(quantity))
        price = result.price
        title = result.title
        units = result.units

        message += '''商品: %(title)s
价格: %(price).2f 元
%(short_url)s
-------------------
''' % locals()

    return message.strip().strip('-------------------')
