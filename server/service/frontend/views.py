# -*- coding: utf-8 -*-
import json
import time

import short_url as short_url
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from stock.restauth.helpers import gen_sign, send_verify_code, check_verify_code
from stock.wechat.models import Member
from wechatpy import WeChatOAuth
from wechatpy import WeChatOAuthException

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def message(request, status='0', message=''):
    data = {'err': status, 'msg': message}
    return HttpResponse(json.dumps(data), content_type="application/json")


def verify(request):
    timestamp = request.POST.get('timestamp')

    openid = request.POST.get('openid')
    mobile = request.POST.get('mobile')
    verify = request.POST.get('verify')

    sign = gen_sign(openid, timestamp)
    print openid, timestamp

    if sign != request.POST.get('sign'):
        return message(request, '-1', '%s => %s' % (sign, request.POST.get('sign')))

    if not verify:
        status, errmsgs = send_verify_code(mobile)
        if status:
            return message(request, message=u"发送成功")
        else:
            return message(request, status='-1', message=errmsgs + 'send')
    else:
        status, msgs = check_verify_code(mobile, verify)

        if status:
            try:
                member = Member.objects.get(openid=openid)
                member.mobile = mobile
                member.save()
                return message(request, status='0', message=u'手机绑定成功')
            except Member.DoesNotExist:
                return message(request, status='-1', message=u'用户不存在')
        else:
            return message(request, status='-1', message=msgs + 'err')


def errors(request):
    return render(request, 'account/errors.html', locals())


def union(request):
    timestamp = request.data.get('timestamp')

    userid = short_url.decode_url(request.data.get('code'))
    remark = request.data.get('remark')
    wechat = request.data.get('alias')

    sign = request.data.get('sign')

    try:
        member = Member.objects.get(pk=userid)

        if gen_sign(member.openid, timestamp) != sign:
            return message(request, status='-1', message='')

        member.remark = remark
        member.wechat = wechat
        member.save()

        return message(request, message='')
    except Member.DoesNotExist:
        return message(request, status='-1', message='')


def success(request, openid):
    try:
        member = Member.objects.filter(openid=openid).get()
        short = short_url.encode_url(member.pk)
        return render(request, 'account/success.html', locals())
    except Member.DoesNotExist:
        return HttpResponseRedirect(redirect_to='/account/signup/')


def signup(request):
    redirect_uri = 'http://wx.gjingxi.com/account/signup/'

    codes = request.GET.get('code', None)
    oauth = WeChatOAuth(settings.WECHAT_APPKEY, settings.WECHAT_SECRET, redirect_uri=redirect_uri,
        scope='snsapi_userinfo')

    if codes is None:
        return HttpResponseRedirect(oauth.authorize_url)

    try:
        access = oauth.fetch_access_token(codes)
        oauth.refresh_access_token(access.get('refresh_token'))
        user = oauth.get_user_info()

        openid = user.get('openid')
        timestamp = int(time.time())
        sign = gen_sign(openid, timestamp)

        member, _ = Member.objects.get_or_create(openid=openid)

        for k, v in user.items():
            if hasattr(member, k):
                setattr(member, k, v)

        member.save()

        if member.mobile:
            return HttpResponseRedirect(redirect_to='/account/success/%s/' % openid)
        else:
            return render(request, 'account/signup.html', locals())

    except WeChatOAuthException as e:
        return HttpResponseRedirect(oauth.authorize_url)
