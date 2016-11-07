#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import requests as req
from fabric.colors import *

BASE_URL = 'http://fa.163.com/interfaces/ngxcache/priceinfo/getRealTimePrice.do?partnerId=njs&goodsId=AG&v=';


def main():
    price = 0.00
    while 1:
        try:
            t = time.time() * 1000
            u = '%s%f' % (BASE_URL, t)
            r = req.get(url=u)
            s = r.json()

            newPrice = float(u"%s" % s['ret']['newPrice'])

            print '>>',

            if price < newPrice:
                print(red('%s' % newPrice))
                up = '↑'
            elif price > newPrice:
                print(green('%s' % newPrice))
                up = '↓'
            else:
                print(white('%s' % newPrice))
                up = '-'

            os.system("osascript -e 'display notification \"价格: %s %s\" with title \"\"'" % (newPrice, up))

            price = newPrice
            time.sleep(5)
        except Exception:
            time.sleep(5)


if __name__ == '__main__':
    main()
