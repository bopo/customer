# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jieba
import short_url

import chatbot

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


def handler(message, *args, **kwargs):
    from service.wechat.models import Member
    code = message['Text'].strip('#')

    try:
        member = Member.objects.get(pk=short_url.decode_url(code))

        if member.remark != '':
            chatbot.send_msg(u'该用户已经绑定过了，请不要重复绑定', message['FromUserName'])
        else:
            remark = code

            chatbot.set_alias(message['FromUserName'], remark)
            chatbot.get_contract(update=True)
            friend = chatbot.search_friends(userName=message['FromUserName'])

            member.wechat = friend.get('Alias')
            member.remark = friend.get('RemarkName')
            member.save()

            chatbot.send_msg(u'恭喜您，已经成功绑定', message['FromUserName'])
    except Member.DoesNotExist:
        chatbot.send_msg(u'对不起, 您确定已经关注过公众号了吗？', message['FromUserName'])
