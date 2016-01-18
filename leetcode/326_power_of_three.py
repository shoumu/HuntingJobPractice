#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/1/18 11:14


import math


def is_power_of_three(n):
    if n < 1:
        return False
    k = math.log(n, 3)
    return abs(round(k) - k) < 1e-10


print(is_power_of_three(243))
