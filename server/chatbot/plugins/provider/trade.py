# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

import jieba
import jieba.posseg as pseg
from django.db.models import Q

from service.kernel.helpers import short_urls
from service.kernel.models import Goods, UNITS_CHOICES

# TOP_APPKEY = settings.WECHAT_APPKEY  # 'wx95d4b735c05ff6a7'
# TOP_SECRET = settings.WECHAT_SECRET  # '5c330e437a2ebf13faf122551b103520'

jieba.initialize()

common_used_numerals_tmp = {u'零': 0, u'一': 1, u'二': 2, u'两': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8,
    u'九': 9,
    u'十': 10, u'百': 100, u'千': 1000, u'万': 10000, u'亿': 100000000}
common_used_numerals = {}

for key in common_used_numerals_tmp:
    common_used_numerals[key] = common_used_numerals_tmp[key]


def chinese2digits(uchars_chinese):
    chinese = ''

    for x in uchars_chinese:
        if x in common_used_numerals_tmp.keys():
            chinese += x

    uchars_chinese = chinese

    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
                # total =total +  r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val

    return total


def handler(message, *args, **kwargs):
    text = message['Text']
    uin = message['FromUserName']
    nick = message.get('ActualNickName') or message.get('NickName')

    seg_list = pseg.cut(text)
    words = []
    quantity = 1

    for word, flag in seg_list:
        if flag == 'm':
            if not re.match(r'\d+', word):
                quantity = chinese2digits(word)
                quantity = re.findall(r'(\d+)', str(quantity))[0]
            else:
                quantity = word
        elif 'n' in flag:
            if word not in UNITS_CHOICES:
                words.append(word)

    print words
    if not words:
        return None

    try:
        queryset = Goods.objects.filter(title__isnull=False)

        for w in words:
            queryset = queryset.filter(Q(title__contains=w) | Q(tags__contains=',%s,' % w))

        result = queryset.all()

        if result:
            result = result[0]
        else:
            raise Goods.DoesNotExist

        # from django.db import connection

        # print connection.queries

        url = 'http://ws.gjingxi.com/buy/?id=%d&q=%d&uin=%s&nick=%s' % (int(result.id), int(quantity), uin, nick)
        # client = WeChatClient(settings.WECHAT_APPKEY, settings.WECHAT_SECRET)
        # short_url = client.misc.short_url(long_url=url)['short_url']
        short_url = short_urls(url)

        amount = float(float(result.price) * float(quantity))
        price = result.price
        title = result.title
        units = result.units

        message = '''商品: %(title)s
价格: %(price).2f 元
数量: %(quantity)s %(units)s
总计: %(amount).2f 元
-----------------------
↓↓ 点击下面链接购买 ↓↓
%(short_url)s''' % locals()
        return message
    except Goods.DoesNotExist:
        return None

# queryset = Goods.objects.filter(title__isnull=False)
#         results = queryset.all()
#
#         if not results:
#             return None
#
#         # from django.db import connection
#
#         # print connection.queries
#         message = '''没有找到您要的商品，下面是本店正在热销的商品
# ===================
# '''
#         quantity = 1
#
#         for result in results:
#             url = 'http://ws.gjingxi.com/buy/?id=%d&q=%d&uin=%s&nick=%s' % (int(result.id), int(quantity), uin, nick)
#             client = WeChatClient(settings.WECHAT_APPKEY, settings.WECHAT_SECRET)
#             short_url = client.misc.short_url(long_url=url)['short_url']
#
#             amount = float(float(result.price) * float(quantity))
#             price = result.price
#             title = result.title
#             units = result.units
#
#             message += '''商品: %(title)s
# 价格: %(price).2f 元
# %(short_url)s
# -------------------
# ''' % locals()
#
#         return message.strip().strip('-------------------')
