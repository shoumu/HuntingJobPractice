#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/16 10:33


def find_min(nums):
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            min_num = nums[i]
            break
    return min_num


nums = [4, 5, 6, 7, 0, 1, 2]
print(find_min(nums))
