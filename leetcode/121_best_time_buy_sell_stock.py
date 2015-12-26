#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/18 10:20


def max_profit(prices):
    min_price = 999999
    max_p = 0
    for price in prices:
        min_price = min(min_price, price)
        max_p = max(max_p, price - min_price)
    return max_p


prices = [7, 2, 4, 1]
print(max_profit(prices))
