# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import re
import time

import itchat
import requests
from django.conf import settings
from fabric.colors import red
from itchat.content import *
from wechatpy import WeChatClient

from chatbot.plugins.handlers import patterns
from chatbot.plugins.provider import goods
from chatbot.plugins.routers import routers

chatbot = itchat.new_instance()


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

        return result
    else:
        return u"知道啦"


@chatbot.msg_register([TEXT, ])
def text_reply(msg):
    for router in routers:
        result = router(msg, patterns)
        print result
        print type(result)

        if result:
            if type(result) == list:
                for res in result:
                    print res
                    chatbot.send_msg(res, msg['FromUserName'])
            else:
                chatbot.send_msg(result, msg['FromUserName'])
        else:
            chatbot.send_msg(tuling_auto_reply(msg['Text']), msg['FromUserName'])


@chatbot.msg_register([NOTE, TEXT, ], isGroupChat=True)
def note_reply(msg):
    print(msg.get('Content'))

    memeber = re.findall(ur'邀请"(.*?)"加入了群聊', msg.get('Content'))
    url = 'http://ws.gjingxi.com/about/criterion/'
    # client = WeChatClient(settings.WECHAT_APPKEY, settings.WECHAT_SECRET)
    # short_url = client.misc.short_url(long_url=url)['short_url']

    if memeber:
        content = u'欢迎加入,'
        # content += u'请遵守本群群规, 点击查看群规 \n%s\n-------------' % url
        # content += goods.handler(msg)
        chatbot.send(u'@%s %s' % (memeber[0], content), msg['FromUserName'])


@chatbot.msg_register(FRIENDS)
def add_friend(msg):
    print('%s 加入好友' % (msg['FromUserName']))
    chatbot.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    chatbot.send_msg('您好！我是全智能客服秘书，请问有什么可以帮助你？', msg['RecommendInfo']['UserName'])
    # chatbot.send_msg('您好！我是全智能客服秘书，请问有什么可以帮助你？!', msg['FromUserName'])
    chatbot.get_contract(update=True)


@chatbot.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    chatbot.get_contract(True)
    if msg['isAt']:
        print('%s At me:%s' % (msg['ActualNickName'], msg['Text']))
        print msg['FromUserName']
        print msg['Text']

        actuals = None
        chatroom = chatbot.update_chatroom(msg['FromUserName'].replace('@@', '@'))

        if chatroom:
            for member in chatroom.get('MemberList'):
                if member.get('NickName') == msg['ActualNickName']:
                    actuals = member
                    break

        if not actuals:
            chatbot.send(u'@%s %s' % (msg['ActualNickName'], u'你还没有加我为好友，加我好友后可以购买'), msg['FromUserName'])
        else:
            result = None

            msg['Text'] = msg['Text'].replace(chatbot.search_friends().get('NickName'), '')

            for router in routers:
                result = router(msg, patterns)
                print result

                if result:
                    chatbot.send_msg(result, msg['FromUserName'])

                    # if not status:
                    #     chatbot.add_friend(userName=actuals['UserName'])
                    #     chatbot.send(u'@%s %s' % (msg['ActualNickName'], u'你还没有加我为好友，加我好友后可以购买'), msg['FromUserName'])
                    #     break

            if not result:
                # content = '已经将购买链接私聊给您了'
                # else:
                content = tuling_auto_reply(msg['Text'].strip('@'))
                NickName = chatbot.search_friends(userName=actuals['UserName'])
                NickName = NickName.get('NickName') if NickName else msg['ActualNickName']
                chatbot.send(u'@%s %s' % (NickName, content), msg['FromUserName'])


def run():
    while True:
        if chatbot.load_login_status(settings.CHATBOT_DEFUALT['SESSION_PATH']):
            chatbot.run(debug=True)
            break
        else:
            print(red(u'用户未登录...退出'))

        time.sleep(10)


if __name__ == '__main__':
    run()
