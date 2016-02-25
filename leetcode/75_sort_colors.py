#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/25 10:08


def sort_colors(nums):
    i, j = (0, 0)
    n = len(nums)
    while i < n and j < n:
        while i < n and nums[i] == 0:
            i += 1
        j = i + 1
        while j < n and nums[j] != 0:
            j += 1
        if i < n and j < n:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
    i, j = (n - 1, n - 1)
    while i >= 0 and j >= 0 and nums[i] != 0 and nums[j] != 0:
        while i >= 0 and nums[i] == 2:
            i -= 1
        j = i - 1
        while 0 <= j and nums[j] != 2:
            j -= 1
        if i >= 0 and j >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j -= 1


def sort_colors_2(nums):
    n = len(nums)
    i, j = 0, n - 1
    while i < j:
        while i < n and nums[i] == 0:
            i += 1
        while j >= 0 and nums[j] == 2:
            j -= 1
        if i < n and j >= 0 and i < j:
            if nums[i] == 1 and nums[j] == 1:
                k = i + 1
                while k < j and nums[k] == 1:
                    k += 1
                if k == j:
                    break
                if nums[k] == 0:
                    nums[i], nums[k] = nums[k], nums[i]
                    i += 1
                else:    # nums[k] == 2
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                if nums[i] == 0:
                    i += 1
                if nums[j] == 2:
                    j -= 1


def sort_colors_3(nums):
    i, j = 0, len(nums) - 1
    for k in range(len(nums)):
        while j > k and nums[k] == 2:
            nums[j], nums[k] = nums[k], nums[j]
            j -= 1
        if nums[k] == 0:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
        if j <= k:
            break



nums = [1, 0, 2, 0, 1]
nums = [0]
nums = [1]
nums = [0, 0]
nums = [1, 1]
nums = [0, 1]
nums = [0, 2]
nums = [1, 2]
nums = [2, 1]
sort_colors_3(nums)
print(nums)