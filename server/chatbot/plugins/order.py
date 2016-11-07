# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jieba

from service.kernel.models import Goods
from service.kernel.models import Orders

TOP_APPKEY = 'wx95d4b735c05ff6a7'
TOP_SECRET = '5c330e437a2ebf13faf122551b103520'
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


def execute(message, uin):
    result = Orders.objects.filter(uin=uin).exclude(status='pay_success').order_by('id', 'desc').all()

    if result:
        if len(result) == 1:
            result = result[0]
            result.number = message
            result.status = 'pay_success'
            result.save()
        else:
            result = result[0]
            result.number = message
            result.status = 'pay_success'
            result.save()

            # url = 'http://wx.gjingxi.com:8099/orders/?&uin=%s' % uin
            # client = WeChatClient(TOP_APPKEY, TOP_SECRET)
            # short_url = client.misc.short_url(long_url=url)['short_url']
        message = '已经完成订单支付操作，已发至工作人员进行核验，核验完成后就给您发货'
    else:
        message = '没有发现您的订单'

    return message

