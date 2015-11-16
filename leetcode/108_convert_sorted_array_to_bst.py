#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/16 10:20


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_bst(nums):
    if not len(nums):
        return None
    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = sorted_array_to_bst(nums[0: middle])
    root.right = sorted_array_to_bst(nums[middle + 1:])
    return root


nums = [1, 2, 3, 4, 5]
root = sorted_array_to_bst(nums)

print(root)