#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/28 21:21


def move_zeros(nums):
    zero = none_zero = 0
    while none_zero < len(nums):
        while zero < len(nums) and nums[zero] != 0:
            zero += 1
        while none_zero < len(nums) and (nums[none_zero] == 0 or none_zero <= zero):
            none_zero += 1
        if zero < len(nums) and none_zero < len(nums):
            nums[zero], nums[none_zero] = nums[none_zero], nums[zero]


# another solution
# just move the none zero number to the head of the array


nums = [0, 1, 0, 3, 12]
nums = [1, 0, 2, 3, 0]
move_zeros(nums)
print(nums)
