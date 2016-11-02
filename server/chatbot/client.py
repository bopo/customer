# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import copy
import hashlib
import io
import json
import mimetypes
import os
import pickle
import re
import sys
import threading
import time
import traceback
import xml.dom.minidom

import pyqrcode
import requests

from . import config, storage, out, tools

BASE_URL = config.BASE_URL


def hash(src):
    m2 = hashlib.md5()
    m2.update(src)
    return m2.hexdigest()


class Client(object):
    def __init__(self):
        self.storage = storage.Storage()
        self.memberList = self.storage.memberList
        self.mpList = self.storage.mpList
        self.chatroomList = self.storage.chatroomList
        self.msgList = self.storage.msgList
        self.loginInfo = {}
        self.request = requests.Session()
        self.uuid = None
        self.debug = False
        self.base_url = 'https://login.weixin.qq.com'

        self.session_hash = None
        self.session_path = 'itchat.kpl'
        self.qr_code_path = 'QR.png'

    def config(self, settings):
        if isinstance(settings, dict):
            for key, val in settings.items():
                if hasattr(self, key.lower()):
                    setattr(self, key.lower(), val)

    def cookies(self):
        return self.request.cookies.items()

    def set_cookies(self, cookies):
        self.request.cookies = cookies

    def dump_login_status(self):

        try:
            with open(self.session_path, 'w') as f:
                f.write('DELETE THIS')

            os.remove(self.session_path)
        except Exception, e:
            traceback.print_exc()
            raise Exception('Incorrect fileDir')

        status = {
            'loginInfo': self.loginInfo,
            'cookies': self.request.cookies.get_dict(),
            'storage': self.storage.dumps()
        }

        with open(self.session_path, 'wb') as f:
            pickle.dump(status, f)

    def load_login_status(self):

        try:
            with open(self.session_path, 'rb') as f:
                j = pickle.load(f)
        except Exception, e:
            traceback.print_exc()
            print self.session_path
            return False

        self.loginInfo = j['loginInfo']
        self.request.cookies = requests.utils.cookiejar_from_dict(j['cookies'])
        self.storage.loads(j['storage'])

        if self.__sync_check():
            print('[+] Login successfully as %s\n' % self.storage.nickName)
            self.start_receiving()
            return True
        else:
            self.request.cookies.clear()
            return False

    def auto_login(self, enableCmdQR=False):
        def open_QR():
            for get_count in range(10):
                out.print_line('Getting uuid', True)

                while not self.get_QRuuid():
                    time.sleep(1)

                print('Getting QR Code')

                if self.get_QR(enableCmdQR=enableCmdQR):
                    break
                elif 9 <= get_count:
                    print('Failed to get QR Code, please restart the program')
                    sys.exit()

            print('Please scan the QR Code')

        open_QR()

        while 1:
            status = self.check_login()

            if status == '200':
                break
            elif status == '201':
                print('Please press confirm')
            elif status == '408':
                print('Reloading QR Code\n')
                open_QR()

        self.web_init()
        self.show_mobile_login()
        self.get_friends(True)

        # 清除终端显示
        tools.clear_screen()
        out.print_line('Login successfully as %s\n' % self.storage.nickName, False)

        self.start_receiving()

    def get_QRuuid(self):
        url = '%s/jslogin' % BASE_URL
        payloads = {'appid': 'wx782c26e4c19acffb', 'fun': 'new', }

        r = self.request.get(url, params=payloads)

        regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
        data = re.search(regx, r.text)

        if data and data.group(1) == '200':
            self.uuid = data.group(2)
            return self.uuid

    def get_QR(self, uuid=None, enableCmdQR=False):
        try:
            if uuid == None:
                uuid = self.uuid

            string = 'https://login.weixin.qq.com/l/' + uuid
            qr = pyqrcode.create(string)

            if enableCmdQR is False:
                qr.show(scale=10)
            else:
                print(qr.terminal(quiet_zone=1))

            return True
        except Exception, e:
            traceback.print_exc()
            raise e

    def check_login(self, uuid=None):
        if uuid is None:
            uuid = self.uuid
        else:
            self.uuid = uuid

        url = '%s/cgi-bin/mmwebwx-bin/login' % BASE_URL
        payloads = 'tip=1&uuid=%s&_=%s' % (uuid, int(time.time()))
        r = self.request.get(url, params=payloads)

        regx = r'window.code=(\d+)'
        data = re.search(regx, r.text)

        print r.text

        if data and data.group(1) == '200':
            if os.path.exists(self.qr_code_path):
                os.remove(self.qr_code_path)

            regx = r'window.redirect_uri="(\S+)";'

            self.loginInfo['url'] = re.search(regx, r.text).group(1)
            r = self.request.get(self.loginInfo['url'], allow_redirects=False)

            print r.text

            self.loginInfo['url'] = self.loginInfo['url'][:self.loginInfo['url'].rfind('/')]
            self.loginInfo['BaseRequest'] = {}

            for node in xml.dom.minidom.parseString(r.text).documentElement.childNodes:
                if node.nodeName == 'skey':
                    self.loginInfo['skey'] = self.loginInfo['BaseRequest']['Skey'] = node.childNodes[0].data
                elif node.nodeName == 'wxsid':
                    self.loginInfo['wxsid'] = self.loginInfo['BaseRequest']['Sid'] = node.childNodes[0].data
                elif node.nodeName == 'wxuin':
                    self.loginInfo['wxuin'] = self.loginInfo['BaseRequest']['Uin'] = node.childNodes[0].data
                elif node.nodeName == 'pass_ticket':
                    self.loginInfo['pass_ticket'] = self.loginInfo['BaseRequest']['DeviceID'] = node.childNodes[0].data

            return '200'

        elif data and data.group(1) == '201':
            return '201'
        elif data and data.group(1) == '408':
            return '408'
        else:
            return '0'

    def web_init(self):
        url = '%s/webwxinit?r=%s' % (self.loginInfo['url'], int(time.time()))

        payloads = {'BaseRequest': self.loginInfo['BaseRequest']}
        headers = {'ContentType': 'application/json; charset=UTF-8'}

        r = self.request.post(url, data=json.dumps(payloads), headers=headers)
        dic = json.loads(r.content.decode('utf-8', 'replace'))
        tools.emoji_formatter(dic['User'], 'NickName')

        self.loginInfo['User'] = tools.struct_friend_info(dic['User'])
        self.loginInfo['SyncKey'] = dic['SyncKey']
        self.loginInfo['synckey'] = '|'.join(['%s_%s' % (item['Key'], item['Val']) for item in dic['SyncKey']['List']])

        self.storage.userName = dic['User']['UserName']
        self.storage.nickName = dic['User']['NickName']

        return dic['User']

    def update_chatroom(self, userName, detailedMember=False):
        url = '%s/webwxbatchgetcontact?type=ex&r=%s' % (self.loginInfo['url'], int(time.time()))
        headers = {'ContentType': 'application/json; charset=UTF-8'}
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Count': 1,
            'List': [{
                'UserName': userName,
                'ChatRoomId': '',
            }],
        }

        r = self.request.post(url, data=json.dumps(payloads), headers=headers)
        j = json.loads(r.content.decode('utf8', 'replace'))['ContactList'][0]

        if detailedMember:
            def get_detailed_member_info(encryChatroomId, memberList):
                url = '%s/webwxbatchgetcontact?type=ex&r=%s' % (self.loginInfo['url'], int(time.time()))
                headers = {'ContentType': 'application/json; charset=UTF-8'}
                payloads = {
                    'BaseRequest': self.loginInfo['BaseRequest'],
                    'Count': len(j['MemberList']),
                    'List': [{'UserName': member['UserName'], 'EncryChatRoomId': j['EncryChatRoomId']} \
                        for member in memberList],
                }
                return json.loads(self.request.post(url, data=json.dumps(payloads), headers=headers
                ).content.decode('utf8', 'replace'))['ContactList']

            MAX_GET_NUMBER = 50
            totalMemberList = []

            for i in range(len(j['MemberList']) / MAX_GET_NUMBER + 1):
                memberList = j['MemberList'][i * MAX_GET_NUMBER: (i + 1) * MAX_GET_NUMBER]
                totalMemberList += get_detailed_member_info(j['EncryChatRoomId'], memberList)

            j['MemberList'] = totalMemberList

        for member in j['MemberList']:
            if self.storage.userName == member['UserName']:
                j['self'] = member

            tools.emoji_formatter(member, 'NickName')
            tools.emoji_formatter(member, 'DisplayName')

        j['isAdmin'] = j['OwnerUin'] == int(self.loginInfo['wxuin'])
        oldIndex = None

        for i, chatroom in enumerate(self.chatroomList):
            if chatroom['UserName'] == j['UserName']:
                oldIndex = i;
                break

        if oldIndex is not None:
            del self.chatroomList[oldIndex]

        self.__update_chatrooms([j])
        self.chatroomList.insert(0, j)
        return j

    def get_contact(self, update=False):
        if 1 < len(self.memberList) and not update:
            return copy.deepcopy(self.memberList)

        url = '%s/webwxgetcontact?r=%s&seq=0&skey=%s' % (self.loginInfo['url'],
        int(time.time()), self.loginInfo['skey'])

        headers = {'ContentType': 'application/json; charset=UTF-8'}
        r = self.request.get(url, headers=headers)
        tempList = json.loads(r.content.decode('utf-8', 'replace'))['MemberList']

        del self.memberList[:]
        del self.mpList[:]

        chatroomList = []
        # chatroomList will not be cleared because:
        # when initializing, it's cleared once
        # when updating, there's not need for clearing
        self.memberList.append(self.loginInfo['User'])

        for m in tempList:
            tools.emoji_formatter(m, 'NickName')

            if m['Sex'] != 0:
                self.memberList.append(m)
            elif not (any([str(n) in m['UserName'] for n in range(10)]) and
                any([chr(n) in m['UserName'] for n in (
                            list(range(ord('a'), ord('z') + 1)) +
                            list(range(ord('A'), ord('Z') + 1)))])):
                continue  # userName have number and str
            elif '@@' in m['UserName']:
                m['isAdmin'] = None  # this value will be set after update_chatroom
                chatroomList.append(m)
            elif '@' in m['UserName']:
                if m['VerifyFlag'] & 8 == 0:
                    self.memberList.append(m)
                else:
                    self.mpList.append(m)

        if chatroomList:
            self.__update_chatrooms(chatroomList)

        return copy.deepcopy(chatroomList)

    def get_friends(self, update=False):
        if update:
            self.get_contact(update=True)

        return copy.deepcopy(self.memberList)

    def get_chatrooms(self, update=False):
        if update:
            self.get_contact(update=True)

        return copy.deepcopy(self.chatroomList)

    def get_mps(self, update=False):
        if update:
            self.get_contact(update=True)

        return copy.deepcopy(self.mpList)

    def show_mobile_login(self):
        url = '%s/webwxstatusnotify' % self.loginInfo['url']
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Code': 3,
            'FromUserName': self.storage.userName,
            'ToUserName': self.storage.userName,
            'ClientMsgId': int(time.time()),
        }

        headers = {'ContentType': 'application/json; charset=UTF-8'}
        r = self.request.post(url, data=json.dumps(payloads), headers=headers)
        return r.status_code == '200'

    # 循环应答
    def start_receiving(self):
        def maintain_loop():
            i = self.__sync_check()
            count = 0
            pauseTime = 1

            while i and count < 4:
                try:
                    if pauseTime < 5:
                        pauseTime += 2

                    if i != '0':
                        msgList = self.__get_msg()

                    if msgList:
                        msgList = self.__produce_msg(msgList)

                        for msg in msgList:
                            self.msgList.insert(0, msg)

                        pauseTime = 1

                    time.sleep(pauseTime)
                    i = self.__sync_check()
                    count = 0
                except requests.exceptions.RequestException as e:
                    if self.debug:
                        traceback.print_exc()

                    count += 1
                    time.sleep(count * 3)
                except Exception as e:
                    out.print_line(str(e), False)
                    if self.debug:
                        traceback.print_exc()

            out.print_line('LOG OUT', False)

        maintainThread = threading.Thread(target=maintain_loop)
        maintainThread.setDaemon(True)
        maintainThread.start()

    # 同步检查
    def __sync_check(self):
        url = '%s/synccheck' % self.loginInfo['url']
        payloads = {
            'r': int(time.time()),
            'skey': self.loginInfo['skey'],
            'sid': self.loginInfo['wxsid'],
            'uin': self.loginInfo['wxuin'],
            'deviceid': self.loginInfo['pass_ticket'],
            'synckey': self.loginInfo['synckey'],
        }

        r = self.request.get(url, params=payloads)

        regx = r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}'
        pm = re.search(regx, r.text)

        if pm.group(1) != '0':
            return None

        return pm.group(2)

    def sync_check(self):
        self.__sync_check()

    def __get_msg(self):
        url = '%s/webwxsync?sid=%s&skey=%s' % (self.loginInfo['url'], self.loginInfo['wxsid'], self.loginInfo['skey'])

        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'SyncKey': self.loginInfo['SyncKey'],
            'rr': int(time.time()),
        }

        headers = {'ContentType': 'application/json; charset=UTF-8'}
        r = self.request.post(url, data=json.dumps(payloads), headers=headers)

        dic = json.loads(r.content.decode('utf-8', 'replace'))
        self.loginInfo['SyncKey'] = dic['SyncKey']

        if dic['AddMsgCount'] != 0:
            return dic['AddMsgList']

    def __produce_msg(self, l):
        rl = []
        srl = [40, 43, 50, 52, 53, 9999]
        # 40 msg, 43 videochat, 50 VOIPMSG, 52 voipnotifymsg, 53 webwxvoipnotifymsg, 9999 sysnotice

        for m in l:
            if '@@' in m['FromUserName'] or '@@' in m['ToUserName']:
                self.__produce_group_chat(m)
            else:
                tools.msg_formatter(m, 'Content')

            if m['MsgType'] == 1:  # words
                if m['Url']:
                    regx = r'(.+?\(.+?\))'
                    data = re.search(regx, m['Content'])
                    data = 'Map' if data is None else data.group(1)
                    msg = {
                        'Type': 'Map',
                        'Text': data,
                    }
                else:
                    msg = {
                        'Type': 'Text',
                        'Text': m['Content'],
                    }
            elif m['MsgType'] == 3 or m['MsgType'] == 47:  # picture
                def download_picture(picDir=None):
                    url = '%s/webwxgetmsgimg' % self.loginInfo['url']
                    payloads = {
                        'MsgID': m['NewMsgId'],
                        'skey': self.loginInfo['skey'],
                    }
                    r = self.request.get(url, params=payloads, stream=True)
                    tempStorage = io.BytesIO()

                    for block in r.iter_content(1024):
                        tempStorage.write(block)

                    if picDir is None:
                        return tempStorage.getvalue()

                    with open(picDir, 'wb') as f:
                        f.write(tempStorage.getvalue())

                msg = {
                    'Type': 'Picture',
                    'FileName': '%s.%s' % (time.strftime('%y%m%d-%H%M%S', time.localtime()),
                    'png' if m['MsgType'] == 3 else 'gif'),
                    'Text': download_picture,
                }
            elif m['MsgType'] == 34:  # voice
                def download_voice(voiceDir=None):
                    url = '%s/webwxgetvoice' % self.loginInfo['url']
                    payloads = {
                        'msgid': m['NewMsgId'],
                        'skey': self.loginInfo['skey'],
                    }

                    r = self.request.get(url, params=payloads, stream=True)
                    tempStorage = io.BytesIO()

                    for block in r.iter_content(1024):
                        tempStorage.write(block)

                    if voiceDir is None:
                        return tempStorage.getvalue()

                    with open(voiceDir, 'wb') as f:
                        f.write(tempStorage.getvalue())

                msg = {
                    'Type': 'Recording',
                    'FileName': '%s.mp4' % time.strftime('%y%m%d-%H%M%S', time.localtime()),
                    'Text': download_voice,
                }
            elif m['MsgType'] == 37:  # friends
                msg = {
                    'Type': 'Friends',
                    'Text': {
                        'status': m['Status'],
                        'userName': m['RecommendInfo']['UserName'],
                        'ticket': m['Ticket'],
                        'userInfo': m['RecommendInfo'],
                    },
                }
            elif m['MsgType'] == 42:  # name card
                msg = {
                    'Type': 'Card',
                    'Text': m['RecommendInfo'],
                }
            elif m['MsgType'] == 49:  # sharing
                if m['AppMsgType'] == 6:
                    def download_atta(attaDir=None):
                        cookiesList = {name: data for name, data in self.request.cookies.items()}
                        url = '/cgi-bin/mmwebwx-bin/webwxgetmedia'

                        if 'web.wechat.com' in self.loginInfo['url']:
                            url = 'https://file.web%s.wechat.com' + url
                        else:
                            url = 'https://file%s.wx.qq.com' + url

                        url = url % ('2' if '2' in self.loginInfo['url'] else '')

                        payloads = {
                            'sender': m['FromUserName'],
                            'mediaid': m['MediaId'],
                            'filename': m['FileName'],
                            'fromuser': self.loginInfo['wxuin'],
                            'pass_ticket': 'undefined',
                            'webwx_data_ticket': cookiesList['webwx_data_ticket'],
                        }

                        r = self.request.get(url, params=payloads, stream=True)
                        tempStorage = io.BytesIO()

                        for block in r.iter_content(1024):
                            tempStorage.write(block)

                        if attaDir is None:
                            return tempStorage.getvalue()

                        with open(attaDir, 'wb') as f:
                            f.write(tempStorage.getvalue())

                    msg = {
                        'Type': 'Attachment',
                        'Text': download_atta,
                    }
                elif m['AppMsgType'] == 17:
                    msg = {
                        'Type': 'Note',
                        'Text': m['FileName'],
                    }
                elif m['AppMsgType'] == 2000:
                    regx = r'\[CDATA\[(.+?)\][\s\S]+?\[CDATA\[(.+?)\]'
                    data = re.search(regx, m['Content'])

                    if data:
                        data = data.group(2).split(u'。')[0]
                    else:
                        data = 'You may found detailed info in Content key.'
                    msg = {
                        'Type': 'Note',
                        'Text': data,
                    }
                else:
                    msg = {
                        'Type': 'Sharing',
                        'Text': m['FileName'],
                    }
            elif m['MsgType'] == 51:  # phone init
                msg = {
                    'Type': 'Init',
                    'Text': m['ToUserName'],
                }
            elif m['MsgType'] == 62:  # tiny video
                def download_video(videoDir=None):
                    url = '%s/webwxgetvideo' % self.loginInfo['url']
                    payloads = {
                        'msgid': m['MsgId'],
                        'skey': self.loginInfo['skey'],
                    }

                    headers = {'Range': 'bytes=0-'}
                    r = self.request.get(url, params=payloads, headers=headers, stream=True)
                    tempStorage = io.BytesIO()

                    for block in r.iter_content(1024):
                        tempStorage.write(block)

                    if videoDir is None:
                        return tempStorage.getvalue()

                    with open(videoDir, 'wb') as f:
                        f.write(tempStorage.getvalue())

                msg = {
                    'Type': 'Video',
                    'FileName': '%s.mp4' % time.strftime('%y%m%d-%H%M%S', time.localtime()),
                    'Text': download_video,
                }
            elif m['MsgType'] == 10000:
                msg = {
                    'Type': 'Note',
                    'Text': m['Content'],
                }
            elif m['MsgType'] == 10002:
                regx = r'\[CDATA\[(.+?)\]\]'
                data = re.search(regx, m['Content'])
                data = 'System message' if data is None else data.group(1).replace('\\', '')
                msg = {
                    'Type': 'Note',
                    'Text': data,
                }
            elif m['MsgType'] in srl:
                msg = {
                    'Type': 'Useless',
                    'Text': 'UselessMsg',
                }
            else:
                out.print_line('MsgType Unknown: %s\n%s' % (m['MsgType'], str(m)), False)
                srl.append(m['MsgType'])
                msg = {
                    'Type': 'Useless',
                    'Text': 'UselessMsg',
                }
            m = dict(m, **msg)
            rl.append(m)

        return rl

    def __produce_group_chat(self, msg):
        r = re.match('(@[0-9a-z]*?):<br/>(.*)$', msg['Content'])

        if not r:
            return

        actualUserName, content = r.groups()

        chatroom = self.storage.search_chatrooms(userName=msg['FromUserName'])
        member = tools.search_dict_list((chatroom or {}).get(
            'MemberList') or [], 'UserName', actualUserName)

        if member is None:
            chatroom = self.update_chatroom(msg['FromUserName'])
            member = tools.search_dict_list((chatroom or {}).get(
                'MemberList') or [], 'UserName', actualUserName)

        msg['ActualUserName'] = actualUserName
        msg['ActualNickName'] = member['DisplayName'] or member['NickName']
        msg['Content'] = content

        tools.msg_formatter(msg, 'Content')
        msg['isAt'] = u'@%s%s' % (chatroom['self']['DisplayName'] or self.storage.nickName,
        u'\u2005' if u'\u2005' in msg['Content'] else ' ') in msg['Content']

    def send_msg(self, msg='Test Message', toUserName=None):
        url = '%s/webwxsendmsg' % self.loginInfo['url']
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Msg': {
                'Type': 1,
                'Content': msg,
                'FromUserName': self.storage.userName,
                'ToUserName': (toUserName if toUserName else self.storage.userName),
                'LocalID': int(time.time()),
                'ClientMsgId': int(time.time()),
            },
        }

        headers = {'ContentType': 'application/json; charset=UTF-8'}
        r = self.request.post(url, data=json.dumps(payloads, ensure_ascii=False).encode('utf8'), headers=headers)

        return r.json()['BaseResponse']['Ret'] == 0

    def __update_chatrooms(self, l):
        oldUsernameList = []
        for chatroom in l:
            # format NickName & DisplayName & self keys
            tools.emoji_formatter(chatroom, 'NickName')
            for member in chatroom['MemberList']:
                if self.storage.userName == member['UserName']:
                    chatroom['self'] = member
                tools.emoji_formatter(member, 'NickName')
                tools.emoji_formatter(member, 'DisplayName')
            # get useful information from old version of this chatroom
            oldChatroom = tools.search_dict_list(
                self.chatroomList, 'UserName', chatroom['UserName'])
            if oldChatroom is not None:
                memberList, oldMemberList = \
                    chatroom['MemberList'], oldChatroom['MemberList']
                # update member list
                if memberList:
                    for member in memberList:
                        oldMember = tools.search_dict_list(
                            oldMemberList, 'UserName', member['UserName'])
                        if oldMember is not None:
                            for k in oldMember:
                                member[k] = member[k] or oldMember[k]
                else:
                    chatroom['MemberList'] = oldMemberList
                # update other info
                for k in oldChatroom:
                    chatroom[k] = chatroom.get(k) or oldChatroom[k]
                # ready for deletion
                oldUsernameList.append(oldChatroom['UserName'])
            # update OwnerUin
            if 'ChatRoomOwner' in chatroom:
                chatroom['OwnerUin'] = tools.search_dict_list(
                    chatroom['MemberList'], 'UserName', chatroom['ChatRoomOwner'])['Uin']
            # update isAdmin
            if 'OwnerUin' in chatroom and chatroom['OwnerUin'] != 0:
                chatroom['isAdmin'] = \
                    chatroom['OwnerUin'] == int(self.loginInfo['wxuin'])
            else:
                chatroom['isAdmin'] = None
        # delete old chatrooms
        oldIndexList = []
        for i, chatroom in enumerate(self.chatroomList):
            if chatroom['UserName'] in oldUsernameList:
                oldIndexList.append(i)
        oldIndexList.sort(reverse=True)
        for i in oldIndexList: del self.chatroomList[i]
        # add new chatrooms
        for chatroom in l:
            self.chatroomList.append(chatroom)

    def __upload_file(self, fileDir, isPicture=False, isVideo=False):
        if not tools.check_file(fileDir):
            return

        url = '/cgi-bin/mmwebwx-bin/webwxuploadmedia?f=json'

        if 'web.wechat.com' in self.loginInfo['url']:
            url = 'https://file.web%s.wechat.com' + url
        else:
            url = 'https://file%s.wx.qq.com' + url

        url = url % ('2' if '2' in self.loginInfo['url'] else '')

        # save it on server
        fileSize = str(os.path.getsize(fileDir))
        cookiesList = {name: data for name, data in self.request.cookies.items()}
        fileType = mimetypes.guess_type(fileDir)[0] or 'application/octet-stream'

        files = {
            'id': (None, 'WU_FILE_0'),
            'name': (None, os.path.basename(fileDir)),
            'type': (None, fileType),
            'lastModifiedDate': (None, time.strftime('%a %b %d %Y %H:%M:%S GMT+0800 (CST)')),
            'size': (None, fileSize),
            'mediatype': (None, 'pic' if isPicture else 'video' if isVideo else'doc'),
            'uploadmediarequest': (None, json.dumps({
                'BaseRequest': self.loginInfo['BaseRequest'],
                'ClientMediaId': int(time.time()),
                'TotalLen': fileSize,
                'StartPos': 0,
                'DataLen': fileSize,
                'MediaType': 4, }, separators=(',', ':'))),
            'webwx_data_ticket': (None, cookiesList['webwx_data_ticket']),
            'pass_ticket': (None, 'undefined'),
            'filename': (os.path.basename(fileDir), open(fileDir, 'rb'), fileType),
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        }

        r = self.request.post(url, files=files, headers=headers)
        return json.loads(r.text)['MediaId']

    def send_file(self, fileDir, toUserName=None):
        if toUserName is None:
            toUserName = self.storage.userName

        mediaId = self.__upload_file(fileDir)

        if mediaId is None:
            return False

        url = '%s/webwxsendappmsg?fun=async&f=json' % self.loginInfo['url']
        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Msg': {
                'Type': 6,
                'Content': (
                    "<appmsg appid='wxeb7ec651dd0aefa9' sdkver=''><title>%s</title>" % os.path.basename(fileDir) +
                    "<des></des><action></action><type>6</type><content></content><url></url><lowurl></lowurl>" +
                    "<appattach><totallen>%s</totallen><attachid>%s</attachid>" % (
                        str(os.path.getsize(fileDir)), mediaId) +
                    "<fileext>%s</fileext></appattach><extinfo></extinfo></appmsg>" % os.path.splitext(fileDir)[
                        1].replace(
                        '.', '')),
                'FromUserName': self.storage.userName,
                'ToUserName': toUserName,
                'LocalID': str(time.time() * 1e7),
                'ClientMsgId': str(time.time() * 1e7),
            },
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        r = self.request.post(url, data=json.dumps(payloads, ensure_ascii=False).encode('utf8'), headers=headers)
        print r.status_code, r.content
        return True
        # return r.status_code == '200'

    def send_image(self, fileDir, toUserName=None):
        if toUserName is None:
            toUserName = self.storage.userName

        mediaId = self.__upload_file(fileDir, isPicture=not fileDir[-4:] == '.gif')

        if mediaId is None:
            return False

        url = '%s/webwxsendmsgimg?fun=async&f=json' % self.loginInfo['url']

        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Msg': {
                'Type': 3,
                'MediaId': mediaId,
                'FromUserName': self.storage.userName,
                'ToUserName': toUserName,
                'LocalID': str(time.time() * 1e7),
                'ClientMsgId': str(time.time() * 1e7),
            },
        }

        if fileDir[-4:] == '.gif':
            url = '%s/webwxsendemoticon?fun=sys' % self.loginInfo['url']
            payloads['Msg']['Type'] = 47
            payloads['Msg']['EmojiFlag'] = 2

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        r = self.request.post(url, data=json.dumps(payloads, ensure_ascii=False).encode('utf8'), headers=headers)
        # return r.status_code == '200'
        return True

    def send_video(self, fileDir, toUserName=None):
        if toUserName is None:
            toUserName = self.storage.userName

        mediaId = self.__upload_file(fileDir, isVideo=True)

        if mediaId is None:
            return False

        url = '%s/webwxsendvideomsg?fun=async&f=json&pass_ticket=%s' % (
            self.loginInfo['url'], self.loginInfo['pass_ticket'])

        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Msg': {
                'Type': 43,
                'MediaId': mediaId,
                'FromUserName': self.storage.userName,
                'ToUserName': toUserName,
                'LocalID': str(time.time() * 1e7),
                'ClientMsgId': str(time.time() * 1e7),
            },
            'Scene': 0,
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
        }

        r = self.request.post(url, data=json.dumps(payloads, ensure_ascii=False).encode('utf8'), headers=headers)
        # return True
        return r.status_code == '200'

    def set_alias(self, userName, alias):
        url = '%s/webwxoplog?lang=%s&pass_ticket=%s' % (
            self.loginInfo['url'], 'zh_CN', self.loginInfo['pass_ticket'])

        data = {
            'UserName': userName,
            'CmdId': 2,
            'RemarkName': alias,
            'BaseRequest': self.loginInfo['BaseRequest'],
        }

        j = self.request.post(url, json.dumps(data, ensure_ascii=False).encode('utf8')).json()
        return j['BaseResponse']['Ret'] == 0

    def add_friend(self, userName, status=2, ticket='', userInfo={}):
        ''' Add a friend or accept a friend
            * for adding status should be 2
            * for accepting status should be 3 '''

        url = '%s/webwxverifyuser?r=%s&pass_ticket=%s' % (
            self.loginInfo['url'], int(time.time()), self.loginInfo['pass_ticket'])

        payloads = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'Opcode': status,  # 3
            'VerifyUserListSize': 1,
            'VerifyUserList': [{
                'Value': userName,
                'VerifyUserTicket': ticket,
            }],
            'VerifyContent': '',
            'SceneListCount': 1,
            'SceneList': 33,  # [33]
            'skey': self.loginInfo['skey'],
        }

        headers = {'ContentType': 'application/json; charset=UTF-8'}
        r = self.request.post(url, data=json.dumps(payloads, ensure_ascii=False), headers=headers)

        if userInfo:  # add user to storage
            self.memberList.append(tools.struct_friend_info(userInfo))

        return r.json()

    def get_head_img(self, userName=None, chatroomUserName=None, picDir=None):
        ''' get head image
         * if you want to get chatroom header: only set chatroomUserName
         * if you want to get friend header: only set userName
         * if you want to get chatroom member header: set both
        '''
        params = {
            'userName': userName or chatroomUserName,
            'skey': self.loginInfo['skey'], }

        url = '%s/webwxgeticon' % self.loginInfo['url']

        if chatroomUserName is None:
            infoDict = self.storage.search_friends(userName=userName)

            if infoDict is None:
                return None
        else:
            if userName is None:
                url = '%s/webwxgetheadimg' % self.loginInfo['url']
            else:
                chatroom = self.storage.search_chatrooms(userName=chatroomUserName)

                if chatroomUserName is None:
                    return None

                if chatroom['EncryChatRoomId'] == '':
                    chatroom = self.update_chatroom(chatroomUserName)

                params['chatroomid'] = chatroom['EncryChatRoomId']

        r = self.request.get(url, params=params, stream=True)
        tempStorage = io.BytesIO()

        for block in r.iter_content(1024):
            tempStorage.write(block)

        if picDir is None:
            return tempStorage.getvalue()

        with open(picDir, 'wb') as f:
            f.write(tempStorage.getvalue())

    def create_chatroom(self, memberList, topic=''):
        url = ('%s/webwxcreatechatroom?pass_ticket=%s&r=%s' % (
            self.loginInfo['url'], self.loginInfo['pass_ticket'], int(time.time())))

        data = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'MemberCount': len(memberList),
            'MemberList': [{'UserName': member['UserName']} for member in memberList],
            'Topic': topic,
        }

        headers = {'content-type': 'application/json; charset=UTF-8'}

        r = self.request.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf8', 'ignore'), headers=headers)
        return r.json()

    def set_chatroom_name(self, chatroomUserName, name):
        url = ('%s/webwxupdatechatroom?fun=modtopic&pass_ticket=%s' % (
            self.loginInfo['url'], self.loginInfo['pass_ticket']))

        data = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'ChatRoomName': chatroomUserName,
            'NewTopic': name,
        }

        headers = {'content-type': 'application/json; charset=UTF-8'}

        return self.request.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf8', 'ignore'),
            headers=headers).json()

    def delete_member_from_chatroom(self, chatroomUserName, memberList):
        url = ('%s/webwxupdatechatroom?fun=delmember&pass_ticket=%s' % (
            self.loginInfo['url'], self.loginInfo['pass_ticket']))

        params = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'ChatRoomName': chatroomUserName,
            'DelMemberList': ','.join([member['UserName'] for member in memberList]),
        }

        headers = {'content-type': 'application/json; charset=UTF-8'}
        return self.request.post(url, data=json.dumps(params), headers=headers).json()

    def add_member_into_chatroom(self, chatroomUserName, memberList):
        url = ('%s/webwxupdatechatroom?fun=addmember&pass_ticket=%s' % (
            self.loginInfo['url'], self.loginInfo['pass_ticket']))

        params = {
            'BaseRequest': self.loginInfo['BaseRequest'],
            'ChatRoomName': chatroomUserName,
            'AddMemberList': ','.join([member['UserName'] for member in memberList]),
        }

        headers = {'content-type': 'application/json; charset=UTF-8'}
        return self.request.post(url, data=json.dumps(params), headers=headers).json()
