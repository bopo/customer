# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import re
import time

import requests
from django.conf import settings
from fabric.colors import red

import chatbot
from chatbot.content import TEXT, FRIENDS

CHATBOT_DEFUALT = {
    'SESSION_PATH': 'runtime/itchat.kpl',
    'QR_CODE_PATH': 'runtime/itchat.png',
    'DEBUG': True,
}


def tuling_auto_reply(msg):
    tuling_key = '94921ef4597846b29674143a133e7158'

    if tuling_key:
        url = "http://www.tuling123.com/openapi/api"

        body = {'key': tuling_key, 'info': msg.encode('utf8'), 'userid': None}

        r = requests.post(url, data=body)

        respond = json.loads(r.text)
        result = ''

        if respond['code'] == 100000:
            result = respond['text'].replace('<br>', '  ')
        elif respond['code'] == 200000:
            result = respond['url']
        elif respond['code'] == 302000:
            for k in respond['list']:
                result = result + u"【" + k['source'] + u"】 " + \
                         k['article'] + "\t" + k['detailurl'] + "\n"
        else:
            result = respond['text'].replace('<br>', '  ')

        print '    ROBOT:', result
        return result
    else:
        return u"知道啦"


@chatbot.msg_register([TEXT, ])
def text_reply(msg):
    # print ('%s:%s' % (itchat.search_friends(userName=msg['FromUserName']).get('NickName'), msg['Text']))

    if re.match(r'\w{5}', msg['Text']):
        content = tuling_auto_reply(msg['Text'])
        chatbot.send_msg(content, msg['FromUserName'])

        # from stock.wechat.models import Member
        # code = msg['Text'].strip('#')
        #
        # try:
        #     member = Member.objects.get(pk=short_url.decode_url(code))
        #
        #     if member.remark != '':
        #         itchat.send_msg(u'该用户已经绑定过了，请不要重复绑定', msg['FromUserName'])
        #     else:
        #         remark = code
        #
        #         itchat.set_alias(msg['FromUserName'], remark)
        #         itchat.get_contract(update=True)
        #         friend = itchat.search_friends(userName=msg['FromUserName'])
        #
        #         member.wechat = friend.get('Alias')
        #         member.remark = friend.get('RemarkName')
        #         member.save()
        #
        #         itchat.send_msg(u'恭喜您，已经成功绑定', msg['FromUserName'])
        # except Member.DoesNotExist:
        #     itchat.send_msg(u'对不起, 您确定已经关注过公众号了吗？', msg['FromUserName'])
    else:
        content = tuling_auto_reply(msg['Text'])
        chatbot.send_msg(content, msg['FromUserName'])


# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@chatbot.msg_register(FRIENDS)
def add_friend(msg):
    logging.info('%s 加入好友' % (msg['FromUserName']))
    chatbot.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    chatbot.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
    chatbot.get_contract(update=True)


@chatbot.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        print msg
        logging.info('%s At me:%s' % (msg['ActualNickName'], msg['Text']))
        content = tuling_auto_reply(msg['Content'])
        chatbot.send(u'@%s %s' % (msg['ActualNickName'], content), msg['FromUserName'])


def run():
    chatbot.default(settings.CHATBOT_DEFUALT)

    while True:
        if chatbot.status():
            chatbot.run(debug=True)
            break
        else:
            print(red(u'用户未登录...退出'))

        time.sleep(10)
