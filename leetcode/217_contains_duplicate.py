#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/1 14:15


"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


def contains_duplicate(nums):
    num_dic = {}
    for num in nums:
        if num_dic.get(num, None):
            return True
        else:
            num_dic[num] = 1
    return False


def contains_duplicate_2(nums):
    return len(nums) != len(set(nums))


nums = [1, 2, 3]
print(contains_duplicate(nums))
