# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os
import time

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()
from django.conf import settings

import requests
from fabric.colors import red

import chatbot
from chatbot.content import TEXT
from chatbot.plugins.handlers import patterns
from chatbot.plugins.routers import routers


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

        if result:
            if type(result, list):
                [chatbot.send_msg(res, msg['FromUserName']) for res in result]
            else:
                chatbot.send_msg(result, msg['FromUserName'])
        else:
            chatbot.send_msg(tuling_auto_reply(msg['Text']), msg['FromUserName'])


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
                    status = chatbot.send_msg(result, actuals['UserName'])

                    if not status:
                        chatbot.add_friend(userName=actuals['UserName'])
                        chatbot.send(u'@%s %s' % (msg['ActualNickName'], u'你还没有加我为好友，加我好友后可以购买'), msg['FromUserName'])
                        return True

            if not result:
                content = tuling_auto_reply(msg['Content'])
            else:
                content = '已经将购买链接私聊给您了'

            NickName = chatbot.search_friends(userName=actuals['UserName'])['NickName']
            chatbot.send(u'@%s %s' % (NickName, content), msg['FromUserName'])


def run():
    chatbot.default(settings.CHATBOT_DEFUALT)

    while True:
        if chatbot.status():
            chatbot.run(debug=True)
            break
        else:
            print(red(u'用户未登录...退出'))

        time.sleep(10)


if __name__ == '__main__':
    run()
