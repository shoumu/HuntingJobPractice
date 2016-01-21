#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/1/21 11:31


def is_power_of_two(n):
    if n >= 1:
        while n % 2 == 0:
            n /= 2
        if n == 1:
            return True
    return False


def is_power_of_two_2(n):
    if n < 1:
        return False
    return n & (n - 1) == 0


def is_power_of_two_3(n):
    if n < 1:
        return False
    return (n & (-n)) == n


print(is_power_of_two_3(1))
print(is_power_of_two_3(2))
print(is_power_of_two_3(3))
print(is_power_of_two_3(8))
