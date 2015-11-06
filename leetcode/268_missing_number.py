#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/6 12:49


def missing_number(nums):
    s = sum(nums)
    return int((1 + len(nums)) * len(nums) / 2 - s)


def missing_number_2(nums):
    s = 0
    for i in range(len(nums)):
        s += (i + 1 - nums[i])
    return s


nums = [0, 1, 3]
print(missing_number_2(nums))
