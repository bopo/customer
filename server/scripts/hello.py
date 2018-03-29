# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from service.kernel.models import Goods


def run():
    goods = Goods.objects.all()
    print goods
    print('hello')
