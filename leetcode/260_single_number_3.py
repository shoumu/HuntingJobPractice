#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/29 12:11


def single_number(nums):
    """
    a very interesting method
    the only appear once number must has some bit that is different, so find this bit and use this bit to group all the
    numbers, and we will get two group that each contains one of the single number, the others must appear twice
    :param nums:
    :return:
    """
    tmp = 0
    for num in nums:
        tmp ^= num
    marker = 1
    while marker & tmp != marker:
        marker <<= 1
    a = 0
    for num in nums:
        if marker & num:
            a ^= num
    b = tmp ^ a
    return [a, b]


nums = [1, 1, 2, 2, 3, 5]
print(single_number(nums))
