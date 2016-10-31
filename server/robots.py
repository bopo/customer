#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright © XYM
# Last modified: 2016-10-24 17:17:25

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import re

import click
import coloredlogs
import django
import environ
import itchat
import requests
import short_url
from itchat.content import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

env = environ.Env()
environ.Env.read_env()

PID_PATH = 'runtime/itchat.kpi'


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


@itchat.msg_register([TEXT, ])
def text_reply(msg):
    print ('%s:%s' % (itchat.search_friends(userName=msg['FromUserName']).get('NickName'), msg['Text']))

    if u'快递' in msg['Text']:
        msgs = u'''
好的，我为你找到几个常用的快递电话。
顺丰：4008111111
申通：95543
韵达：400-821-6789
中通：4008-270-270
EMS：11183
全峰：400-100-0001
宅急送：400-6789-000
天天：4001-888-888        
        '''
        itchat.send_msg(msgs, msg['FromUserName'])
    elif re.match(r'^\d{10,}$', msg['Text']):
        msgs = u'''点击下面链接查看快递: 
http://m.kuaidi100.com/index_all.html?type=&postid=%s&callbackurl=http://www.gjingxi.com
        ''' % msg['Text']
        itchat.send_msg(msgs, msg['FromUserName'])
    elif re.match(r'\w{5}', msg['Text']):
        from stock.wechat.models import Member
        code = msg['Text'].strip('#')

        try:
            member = Member.objects.get(pk=short_url.decode_url(code))

            if member.remark != '':
                itchat.send_msg(u'该用户已经绑定过了，请不要重复绑定', msg['FromUserName'])
            else:
                remark = code

                itchat.set_alias(msg['FromUserName'], remark)
                itchat.get_contract(update=True)
                friend = itchat.search_friends(userName=msg['FromUserName'])

                member.wechat = friend.get('Alias')
                member.remark = friend.get('RemarkName')
                member.save()

                itchat.send_msg(u'恭喜您，已经成功绑定', msg['FromUserName'])
        except Member.DoesNotExist:
            itchat.send_msg(u'对不起, 您确定已经关注过公众号了吗？', msg['FromUserName'])
    else:
        content = tuling_auto_reply(msg['Text'])
        itchat.send_msg(content, msg['FromUserName'])


# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    logging.info('%s 加入好友' % (msg['FromUserName']))
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
    itchat.get_contract(update=True)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        print msg
        logging.info('%s At me:%s' % (msg['ActualNickName'], msg['Text']))
        content = tuling_auto_reply(msg['Content'])
        itchat.send(u'@%s %s' % (msg['ActualNickName'], content), msg['FromUserName'])


@click.command()
@click.option('-p', '--pid', default='itchat.kpi', help='runtime file.')
@click.option('-l', '--login', is_flag=True, help='only login.')
@click.option('-d', '--debug', is_flag=True, help='debug mode.')
@click.option('-v', '--verbose', count=True)
def main(login, debug, verbose, pid):
    if debug:
        logging.getLogger(__name__)
        coloredlogs.install(level='DEBUG')

    itchat.pid(pid)
    itchat.login(enableCmdQR=True, hotReload=True)

    if not login:
        itchat.run(debug=debug)


if __name__ == '__main__':
    main()
