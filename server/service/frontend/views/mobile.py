# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

import chatbot

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

CHATBOT_DEFUALT = settings.CHATBOT_DEFUALT
chatbot.default(CHATBOT_DEFUALT)


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
    print chatbot.cookies()
    uuid = chatbot.get_QRuuid()
    return render(request, 'mobile/qr_login.html', locals())


def qr_check(request, uuid):

    response = chatbot.check_login(uuid=uuid)

    if response == '200':
        print chatbot.__client.loginInfo
        print chatbot.web_init()
        print chatbot.show_mobile_login()
        print chatbot.dump_login_status()
        print chatbot.get_friends(True)
        print chatbot.__client.loginInfo

    return HttpResponse(response)


def qr_done(request):
    return render(request, 'mobile/qr_done.html', locals())
