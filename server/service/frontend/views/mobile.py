# -*- coding: utf-8 -*-
import json
import uuid

from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from wechatpy import WeChatOAuth

import itchat
from service.kernel.models import Goods
from service.kernel.models import Orders

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

# chatbot.default(settings.CHATBOT_DEFUALT)
chatbot = itchat.new_instance()


# @cache_page(60 * 15)
def home(request):
    return render(request, 'mobile/index.html', locals())


def history(request):
    return render(request, 'mobile/history.html', locals())


def report(request):
    return render(request, 'mobile/report.html', locals())


def me(request):
    return render(request, 'mobile/me.html', locals())


def support(request):
    return render(request, 'mobile/support.html', locals())


def qr_login(request):
    uuid = chatbot.get_QRuuid()
    return render(request, 'mobile/qr_login.html', locals())


def qr_check(request, uuid):
    response = chatbot.check_login(uuid=uuid)

    if response == '200':
        print chatbot.web_init()
        print chatbot.show_mobile_login()
        print chatbot.get_contact(True)
        print chatbot.dump_login_status(fileDir=settings.CHATBOT_DEFUALT['SESSION_PATH'])

        # chatbot.auto_login(hotReload=True, statusStorageDir='runtime/chatbot.pkl')

    return HttpResponse(response)


def qr_done(request):
    return render(request, 'mobile/qr_done.html', locals())


# 商品列表
def goods(request):
    goods_list = Goods.objects.all()
    return render(request, 'mobile/goods.html', locals())


# 商品详细
def detail(request, id):
    detail = get_object_or_404(Goods, pk=id)
    return render(request, 'mobile/detail.html', locals())


# 商品购买
def buy(request):
    code_ = request.GET.get('code', None)
    oauth = WeChatOAuth(settings.WECHAT_APPKEY, settings.WECHAT_SECRET,
        redirect_uri=request.build_absolute_uri(request.get_full_path()))

    if code_ is None:
        return HttpResponseRedirect(oauth.authorize_url)

    access = oauth.fetch_access_token(code_)
    oauth.refresh_access_token(access.get('refresh_token'))
    user = oauth.get_user_info()

    request.session['openid'] = user.get('openid')
    # nick = user.get('nickname')

    items = get_object_or_404(Goods, pk=request.GET.get('id'))
    items.quantity = request.GET.get('q')
    items.amount = float(float(items.price) * float(items.quantity))
    items.nick = user.get('nickname')

    return render(request, 'mobile/buy/pay.html', locals())


def buy_save(request):
    print request.method
    amount = 12
    if request.method == 'POST':
        # openid = request.session.get('openid')
        # uin = request.POST.get('uin', 'NULL')

        id = request.POST.get('id')
        items = get_object_or_404(Goods, pk=id)
        quantity = request.POST.get('quantity')
        amount = float(float(items.price) * float(quantity))
        nick = request.POST.get('nick')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        orders = Orders.objects.create(goods_id=id)
        # orders.uin = uin
        orders.nick = nick
        orders.token = uuid.uuid1()
        orders.mobile = mobile
        # orders.openid = openid
        orders.amount = str(amount)
        orders.address = address
        orders.quantity = quantity
        orders.save()

        if not orders:
            raise Http404

        return HttpResponse(json.dumps({'amount': amount}), content_type='application/json')
    else:
        raise Http404


def buy_confirm(request, token):
    # code_ = request.GET.get('code', None)
    # oauth = WeChatOAuth(settings.WECHAT_APPKEY, settings.WECHAT_SECRET,
    #     redirect_uri=request.build_absolute_uri(request.get_full_path()))
    #
    # if code_ is None:
    #     return HttpResponseRedirect(oauth.authorize_url)
    #
    # access = oauth.fetch_access_token(code_)
    # oauth.refresh_access_token(access.get('refresh_token'))
    # user = oauth.get_user_info()
    #
    # request.session['openid'] = user.get('openid')
    # -----------------------------------------------
    orders = get_object_or_404(Orders, token=token)
    return render(request, 'mobile/buy/confirm.html', locals())


def buy_success(request, token):
    orders = get_object_or_404(Orders, token=token)
    return render(request, 'mobile/buy/success.html', locals())


def buy_errors(request):
    return render(request, 'mobile/buy/errors.html', locals())


def buy_close(request, token):
    result = Orders.objects.filter(token=token)

    if result:
        result.delete()
        data = {'error': '0'}
    else:
        data = {'error': '1'}

    return JsonResponse(data=data)


def MP_verify_6GR663zqKDgj54ic(request):
    data = open('MP_verify_6GR663zqKDgj54ic.txt').read()
    return HttpResponse(data)
