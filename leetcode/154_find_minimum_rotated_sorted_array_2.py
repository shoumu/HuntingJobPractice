#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/1 9:59


def find_min(nums):
    min_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            min_num = nums[i]
            break
    return min_num


def find_min_2(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[start]:
            end = mid
        else:
            end -= 1
    return nums[start]


test_nums = [2, 3, 4, 5, 6, 0, 1, 2]
test_nums = [0, 1, 2, 3]
test_nums = [2, 2, 2, 1, 2]
test_nums = [1, 3, 3]
print(find_min_2(test_nums))
