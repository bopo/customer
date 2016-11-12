# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Express:
    @staticmethod
    def process(message):
        return message


def handler(message, *args, **kwargs):
    text = message['Text']
    uin = message['FromUserName']
    pass
