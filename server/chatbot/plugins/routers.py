# coding:utf-8

import re


# ---------------- 参考 -----------------
# 参考信息：
# 消息类型：text, event, image, video, link , location,
def base_router(recv_msg, router_patterns):
    for type, key, handler in router_patterns:
        if re.search(key, recv_msg['Text']):
            result = handler(recv_msg, router_patterns)
            if result:
                return result


# def new_msg_from_db(pattern):
#     """Convert PicTextMsg from db to PicTextMsg object for rendering"""
#     items = []
#
#     for item in pattern.handler.all():
#         items.append(PTItem(item.title, item.description, item.pic_url, item.url))
#
#     return items


# def db_router(recv_msg, *args):
#     # 文本类型
#     if recv_msg.msg_type == 'text':
#         for pattern in PatternT2T.objects.all():
#             match = re.search(pattern.content.encode('utf-8'), recv_msg.content)
#
#             if match:
#                 return text_response(recv_msg, pattern.handler.content)
#
#         for pattern in PatternT2PT.objects.all():
#             match = re.search(pattern.content.encode('utf-8'), recv_msg.content)
#
#             if match:
#                 return text_response(recv_msg, new_msg_from_db(pattern))


routers = [base_router, ]
