#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/29 17:12


def permue(nums):
    res = []
    if nums:
        help(nums, res, [])
    return res


def help(nums, res, cur):
    if len(cur) is len(nums):
        res.append(list(cur))
    for num in nums:
        if num in cur:
            continue
        cur.append(num)
        help(nums, res, cur)
        cur.pop()


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(permue(nums))
