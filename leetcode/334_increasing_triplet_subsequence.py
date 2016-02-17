#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 16/2/17 23:49


def increasing_triplet(nums):
    small = 9999999999
    big = 9999999999
    for num in nums:
        if num <= small:
            small = num
        elif num <= big:
            big = num
        else:
            return True
    return False


print(increasing_triplet([1, 0, 0, 0, 0, 1000]))
