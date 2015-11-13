#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/13 10:10


def max_sub_array(nums):
    max_sum = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
        max_sum = max(nums[i], max_sum)
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))
