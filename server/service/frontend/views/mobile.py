# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

import chatbot
from service.kernel.models import Goods
from service.kernel.models import Orders

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


def support(request):
    return render(request, 'mobile/support.html', locals())


def qr_login(request):
    print chatbot.cookies()
    uuid = chatbot.get_QRuuid()
    return render(request, 'mobile/qr_login.html', locals())


def qr_check(request, uuid):
    response = chatbot.check_login(uuid=uuid)

    if response == '200':
        print chatbot.web_init()
        # print chatbot.__client.show_mobile_login()
        print chatbot.dump_login_status()
        # print chatbot.get_friends(True)
        # print chatbot.__client.loginInfo

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

    items = get_object_or_404(Goods, pk=request.GET.get('id'))
    items.quantity = request.GET.get('q')
    items.amount = float(float(items.price) * float(items.quantity))

    return render(request, 'mobile/buy/pay.html', locals())


def buy_save(request):
    if request.method == 'POST':
        openid = request.session.get('openid')
        id = request.POST.get('id')
        uin = request.POST.get('uin', 'NULL')
        items = get_object_or_404(Goods, pk=id)
        quantity = request.POST.get('quantity')
        amount = float(float(items.price) * float(quantity))

        orders = Orders.objects.create(goods_id=id, uin=uin, openid=openid, quantity=quantity, amount=amount,
            token=uuid.uuid1())

        if not orders:
            raise Http404

        return redirect(reverse('buy_success', args=[orders.token]))

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
