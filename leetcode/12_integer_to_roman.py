#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/12 12:38


def int_to_roman(num):
    num_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    code_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    roman = ''
    for i in range(12, -1, -1):
        while num >= num_list[i]:
            roman += code_list[i]
            num -= num_list[i]
        if num == 0:
            break
    return roman


print(int_to_roman(3999))
