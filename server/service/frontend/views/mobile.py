# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

import itchat

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

CHATBOT_DEFUALT = settings.CHATBOT_DEFUALT
itchat.default(CHATBOT_DEFUALT)


# @cache_page(60 * 15)
# @oauth
def home(request):
    return render(request, 'mobile/index.html', locals())


def history(request):
    return render(request, 'mobile/history.html', locals())


def report(request):
    return render(request, 'mobile/report.html', locals())


def me(request):
    return render(request, 'mobile/me.html', locals())


def qr_login(request):
    print itchat.cookies()
    uuid = itchat.get_QRuuid()
    return render(request, 'mobile/qr_login.html', locals())


def qr_check(request, uuid):
    uuid += '=='
    print uuid

    # if itchat.status():
    #     return HttpResponse('405')

    response = itchat.check_login(uuid=uuid)

    if response == '200':
        print itchat.__client.loginInfo
        print itchat.web_init()
        print itchat.show_mobile_login()
        print itchat.dump_login_status()
        # print itchat.get_friends(True)
        print itchat.__client.loginInfo

    return HttpResponse(response)


def qr_done(request):
    return render(request, 'mobile/qr_done.html', locals())
