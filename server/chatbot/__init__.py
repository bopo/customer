# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import time

import sys

from . import content
from .client import Client

__version__ = '1.1.17'

__client = Client()

HOT_RELOAD = False


def login(hotReload=False, enableCmdQR=False):
    global HOT_RELOAD
    if hotReload:
        if __client.load_login_status():
            return

        __client.auto_login(enableCmdQR=enableCmdQR)
        __client.dump_login_status()  # 写入登录请求对象
        HOT_RELOAD = True
    else:
        __client.auto_login(enableCmdQR=enableCmdQR)
        HOT_RELOAD = False


def status():
    if not os.path.exists(__client.session_path):
        logging.debug('[!] 没有 session 文件 ... 关闭')
        # sys.exit()

    if __client.load_login_status():
        return True

    return False


def default(conf):
    __client.config(conf)


# The following method are all included in __client.auto_login >>>
def get_QRuuid():
    return __client.get_QRuuid()


def get_QR(uuid=None, enableCmdQR=False):
    return __client.get_QR(uuid, enableCmdQR)


def check_login(uuid=None):
    return __client.check_login(uuid)


def web_init():
    return __client.web_init()


def cookies():
    return __client.cookies()


def start_receiving():
    return __client.start_receiving()


def dump_login_status():
    return __client.dump_login_status()


def load_login_status():
    return __client.load_login_status()


def user_sync_check():
    return __client.sync_check()


def get_friends(update=False):
    return __client.get_friends(update)


def search_friends(name=None, userName=None, remarkName=None, nickName=None, wechatAccount=None):
    return __client.storage.search_friends(name, userName, remarkName, nickName, wechatAccount)


def set_alias(userName, alias):
    return __client.set_alias(userName, alias)


def add_friend(userName, status=2, ticket='', userInfo={}):
    return __client.add_friend(userName, status, ticket, userInfo)


def get_head_img(userName=None, chatroomUserName=None, picDir=None):
    return __client.get_head_img(userName, chatroomUserName, picDir)


def get_mps(update=False):
    return __client.get_mps(update)


def search_mps(name=None, userName=None):
    return __client.storage.search_mps(name, userName)


def get_chatrooms(update=False):
    return __client.get_chatrooms(update)


def search_chatrooms(name=None, userName=None):
    return __client.storage.search_chatrooms(name, userName)


def update_chatroom(groupUserName, detailedMember=False):
    return __client.update_chatroom(groupUserName, detailedMember)


def create_chatroom(memberList, topic=''):
    return __client.create_chatroom(memberList, topic)


def set_chatroom_name(chatroomUserName, name):
    return __client.set_chatroom_name(chatroomUserName, name)


def delete_member_from_chatroom(chatroomUserName, memberList):
    return __client.delete_member_from_chatroom(chatroomUserName, memberList)


def add_member_into_chatroom(chatroomUserName, memberList):
    return __client.add_member_into_chatroom(chatroomUserName, memberList)


def get_contract(update=False):
    return __client.get_friends(update)


def get_batch_contract(groupUserName):
    return __client.update_chatroom(groupUserName)


def send_msg(msg='Test Message', toUserName=None):
    return __client.send_msg(msg, toUserName)


def send_file(fileDir, toUserName):
    return __client.send_file(fileDir, toUserName)


def send_video(fileDir, toUserName):
    return __client.send_video(fileDir, toUserName)


def send_image(fileDir, toUserName):
    return __client.send_image(fileDir, toUserName)


def send(msg, toUserName=None):
    if msg is None:
        return False

    if msg[:5] == '@fil@':
        return __client.send_file(msg[5:], toUserName)
    elif msg[:5] == '@img@':
        return __client.send_image(msg[5:], toUserName)
    elif msg[:5] == '@msg@':
        return __client.send_msg(msg[5:], toUserName)
    elif msg[:5] == '@vid@':
        return __client.send_video(msg[5:], toUserName)
    else:
        return __client.send_msg(msg, toUserName)


__functionDict = {'FriendChat': {}, 'GroupChat': {}, 'MpChat': {}}


def configured_reply():
    ''' determine the type of message and reply if its method is defined
        however, I use a strange way to determine whether a msg is from massive platform
        I haven't found a better solution here
        The main problem I'm worrying about is the mismatching of new friends added on phone
        If you have any good idea, pleeeease report an issue. I will be more than grateful.
    '''
    if not __client.storage.msgList:
        return

    msg = __client.storage.msgList.pop()

    if '@@' in msg['FromUserName']:
        replyFn = __functionDict['GroupChat'].get(msg['Type'])

        if replyFn:
            send(replyFn(msg), msg.get('FromUserName'))

    elif search_mps(userName=msg['FromUserName']):
        replyFn = __functionDict['MpChat'].get(msg['Type'])

        if replyFn:
            send(replyFn(msg), msg.get('FromUserName'))
    else:
        replyFn = __functionDict['FriendChat'].get(msg['Type'])

        if replyFn:
            send(replyFn(msg), msg.get('FromUserName'))


def msg_register(msgType, isFriendChat=False, isGroupChat=False, isMpChat=False):
    ''' a decorator constructor
        return a specific decorator based on information given
    '''
    if not isinstance(msgType, list):
        msgType = [msgType]

    def _msg_register(fn):
        for _msgType in msgType:
            if isFriendChat:
                __functionDict['FriendChat'][_msgType] = fn

            if isGroupChat:
                __functionDict['GroupChat'][_msgType] = fn

            if isMpChat:
                __functionDict['MpChat'][_msgType] = fn

            if not any((isFriendChat, isGroupChat, isMpChat)):
                __functionDict['FriendChat'][_msgType] = fn

    return _msg_register


# in-build run
def run(debug=True):
    print('Start auto replying')

    __client.debug = debug

    try:
        while 1:
            if not check_login():
                print('\rLOG OUT')
                break
            configured_reply()
            time.sleep(.3)
    except KeyboardInterrupt:
        if HOT_RELOAD:
            __client.dump_login_status()

        print('\rBye~')
