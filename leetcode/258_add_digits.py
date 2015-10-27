#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/27 11:14


def add_digits(num):
    if num is 0:
        return 0
    elif num % 9 is 0:
        return 9
    else:
        return num % 9

print(add_digits(22))
