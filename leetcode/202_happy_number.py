#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/14 14:33


def is_happy(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    num = n
    seen = set()
    while num not in seen:
        seen.add(num)
        num_str = str(num)
        num = 0
        for ch in num_str:
            num += (int(ch) * int(ch))
        if num == 1:
            return True
    return False


def is_happy_2(n):
    if n <= 0:
        return False
    while n >= 10:
        sum = 0
        while n != 0:
            sum += (n % 10) * (n % 10)
            n /= 10
        n = sum
    return n == 1 or n == 7

print(is_happy_2(18))
