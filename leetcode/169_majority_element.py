#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/9 11:29


def majority_element(nums):
    nums.sort()
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count > len(nums) / 2:
            return nums[i]
    return nums[0]


def majority_element_2(nums):
    """
    Good job
    :param nums:
    :return:
    """
    cur = 0
    count = 0
    for n in nums:
        if count == 0:
            cur = n
            count += 1
        elif cur == n:
            count += 1
        else:
            count -= 1
    return cur


nums = [1, 2, 1]
print(majority_element(nums))
