# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from wechatpy import WeChatClient

from service.kernel.models import Goods


# TOP_APPKEY = settings.WECHAT_APPKEY  # 'wx95d4b735c05ff6a7'
# TOP_SECRET = settings.WECHAT_SECRET  # '5c330e437a2ebf13faf122551b103520'



def handler(message, *args, **kwargs):
    queryset = Goods.objects.filter(title__isnull=False)
    results = queryset.all()

    if not results:
        return None

    message = '''
===================
本群最新团购商品如下
===================
'''
    quantity = 1

    for result in results:
        url = 'http://ws.gjingxi.com/buy/?id=%d&q=%d&uin=%s&nick=%s' % (int(result.id), int(quantity), '', '')
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
