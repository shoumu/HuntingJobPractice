#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/11 11:49


def single_number(nums):
    ones = 0
    twos = 0
    threes = 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return ones


nums = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
print(single_number(nums))
