# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from stock.service.models.stock import Basic
import tushare as ts


def run():
    '''
    批量导入股票基本面

    :return:
    '''
    data = ts.get_stock_basics()
    
    for index, row in data.iterrows():
        obj, _ = Basic.objects.get_or_create(code=index)
        
        for col_name in data.columns:
            if hasattr(obj, col_name):
                setattr(obj, col_name, row[col_name])

        obj.save()
        print index
