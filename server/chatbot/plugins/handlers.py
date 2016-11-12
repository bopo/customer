#!/usr/bin/env python
# coding:utf-8
import re


def help_handler(recv_msg, *args, **kwargs):
    content = u"""
    --帮助提示--
    """
    return content


from .provider import trade, express, orders, account

patterns = [
    # 消息类型  消息文字（非文字类型消息留空）  操作函数
    ('text', re.compile(r'\d{10,}'), express.handler),
    ('text', re.compile(r'\d{28,}'), orders.handler),
    ('text', re.compile(r'\w{5}$'), account.handler),
    ('text', re.compile(ur'^help|帮助$'), help_handler),
    ('text', '', trade.handler),
]
