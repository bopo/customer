# -*- coding: utf-8 -*-

from django.shortcuts import render
# from . import oauth

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

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
