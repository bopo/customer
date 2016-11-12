# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import time

import requests
from django.conf import settings
from fabric.colors import red

import chatbot
from chatbot.content import TEXT, FRIENDS
from chatbot.plugins.handlers import patterns, help_handler as default_handler
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
    # print ('%s:%s' % (itchat.search_friends(userName=msg['FromUserName']).get('NickName'), msg['Text']))
    print msg['FromUserName']
    print msg['Text']

    ############################
    # routers = [base_router, db_router]

    for router in routers:
        result = router(msg, patterns)
        print result

        if result:
            chatbot.send_msg(result, msg['FromUserName'])

    content = tuling_auto_reply(msg['Text'])
    chatbot.send_msg(content, msg['FromUserName'])

    return default_handler(msg)
    ############################

    # message = trade.execute(message=msg['Text'].encode('utf-8'), uin=msg['FromUserName'])
    #
    # if message:
    #     print message
    #     chatbot.send(message, msg['FromUserName'])
    # elif re.match(r'\d{10,}', msg['Text']):
    #     # message = express.execute(message=msg['Text'].encode('utf-8'), uin=msg['FromUserName'])
    #
    #     # if message:
    #     #     chatbot.send(message, msg['FromUserName'])
    #     pass
    # elif re.match(r'\d{28}', msg['Text']):
    #     message = orders.execute(message=msg['Text'].encode('utf-8'), uin=msg['FromUserName'])
    #
    #     if message:
    #         chatbot.send(message, msg['FromUserName'])
    # elif re.match(r'\w{5}', msg['Text']):
    #     content = tuling_auto_reply(msg['Text'])
    #     chatbot.send_msg(content, msg['FromUserName'])
    #
    #
    # else:
    #     content = tuling_auto_reply(msg['Text'])
    #     chatbot.send_msg(content, msg['FromUserName'])


@chatbot.msg_register(FRIENDS)
def add_friend(msg):
    print('%s 加入好友' % (msg['FromUserName']))
    chatbot.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    chatbot.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
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
