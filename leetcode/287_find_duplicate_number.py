#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/14 10:27


def find_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return nums[i]


def find_duplicate_2(nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            return finder



nums = [1, 2, 3, 4, 4, 5]
nums = [1, 3, 4, 2, 2]
nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
print(find_duplicate_2(nums))
