#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/10 21:48


def is_ugly(num):
    if num <= 0:
        return False
    while num % 2 is 0:
        num //= 2
    while num % 3 is 0:
        num //= 3
    while num % 5 is 0:
        num //= 5
    if num is 1:
        return True
    else:
        return False


print(is_ugly(0))
print(is_ugly(6))
print(is_ugly(14))
