#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/8 11:14

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.get_height(root.left) - self.get_height(root.right)) <= 1 \
                and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def get_height(self, node):
        if not node:
            return 0
        else:
            return max(self.get_height(node.left) + 1, self.get_height(node.right) + 1)
