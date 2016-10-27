# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from stock.service.models.stock import Term


def run():
    for x in open('stock_terms.jl'):
        j = json.loads(x)
        obj, _ = Term.objects.get_or_create(keyword=j.get('name'))
        obj.content = j.get('body').replace('<br/ >', "\n").replace('<br>', "\n").replace('<br/>', "\n").replace('<p>', '').replace('</p>', '')
        obj.save()
        print obj.keyword
        del obj
