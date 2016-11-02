# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

import itchat
from scripts.wechat import CHATBOT_DEFUALT


def run():
    itchat.default(CHATBOT_DEFUALT)
    # itchat.login(hotReload=True, enableCmdQR=False)
    # print itchat.cookies()
    # uuid = itchat.get_QRuuid()
    # print 'https://login.weixin.qq.com/qrcode/' + uuid
    # print itchat.cookies()

    for x in range(10):
        print itchat.check_login('YbEgRPUP1Q==')
        print itchat.cookies()
        time.sleep(3)
