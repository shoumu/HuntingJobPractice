#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/26 16:50


def bulb_switch(n):
    i = 1
    while i * i <= n:
        i += 1
    return i - 1


print(bulb_switch(9999))
print(bulb_switch(9999999999999))