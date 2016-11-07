# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import os
import re
import platform
import click
import coloredlogs
import django
import environ
import chatbot
import requests
import short_url
from chatbot.content import *
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

from django.conf import settings
env = environ.Env()
environ.Env.read_env()

PID_PATH = 'chatbot.kpi'


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

        # print '    ROBOT:', result
        return result
    else:
        return u"知道啦"



def say(msg):
    if platform.system() == 'Darwin':
        # os.system('say %s' % msg)
        print(msg)
        os.system('say "' + msg+'"')
    else:
        print(msg)

@chatbot.msg_register([TEXT, ])
def text_reply(msg):
    say("网友说:" + msg['Text'])

    if re.match(r'\w{5}', msg['Text']):
        from stock.wechat.models import Member
        code = msg['Text'].strip('#')

        try:
            member = Member.objects.get(pk=short_url.decode_url(code))

            if member.remark != '':
                chatbot.send_msg(u'该用户已经绑定过了，请不要重复绑定', msg['FromUserName'])
            else:
                remark = code

                chatbot.set_alias(msg['FromUserName'], remark)
                chatbot.get_contract(update=True)
                friend = chatbot.search_friends(userName=msg['FromUserName'])

                member.wechat = friend.get('Alias')
                member.remark = friend.get('RemarkName')
                member.save()

                chatbot.send_msg(u'恭喜您，已经成功绑定', msg['FromUserName'])
        except Member.DoesNotExist:
            chatbot.send_msg(u'对不起, 您确定已经关注过公众号了吗？', msg['FromUserName'])
    else:
        content = tuling_auto_reply(msg['Text'])
        say('我说:%s' % content)
        chatbot.send_msg(content, msg['FromUserName'])


# @chatbot.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@chatbot.msg_register(FRIENDS)
def add_friend(msg):
    logging.info(u'%s 加入好友' % (msg['FromUserName']))
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


@click.command()
@click.option('-p', '--pid', default='chatbot.kpi', help='runtime file.')
@click.option('-l', '--login', is_flag=True, help='only login.')
@click.option('-d', '--debug', is_flag=True, help='debug mode.')
@click.option('-v', '--verbose', count=True)
def main(login, debug, verbose, pid):
    if debug:
        logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG')

    chatbot.default(settings.CHATBOT_DEFUALT)
    chatbot.login(enableCmdQR=True, hotReload=True)

    if not login:
        chatbot.run(debug=debug)


if __name__ == '__main__':
    main()
