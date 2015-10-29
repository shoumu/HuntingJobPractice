#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/29 11:59


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_tree(root):
    if root:
        root.left, root.right = root.right, root.left
        if root.left:
            invert_tree(root.left)
        if root.right:
            invert_tree(root.right)
    return root

root = TreeNode(1)
