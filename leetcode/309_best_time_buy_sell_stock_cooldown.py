#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/31 12:43


def max_profit(prices):
    if len(prices) < 2:
        return 0
    last = dlast = 0
    for i in range(1, len(prices)):
        temp = last
        if last + prices[i] - prices[i - 1] > dlast:
            last = last + prices[i] - prices[i - 1]
        else:
            last = dlast
        if temp > dlast:
            dlast = temp
    if dlast > last:
        return dlast
    else:
        return last


prices = [1, 2, 3, 0, 2]
print(max_profit(prices))
