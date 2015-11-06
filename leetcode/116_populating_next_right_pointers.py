#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/6 13:26


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    row_start = root
    while row_start:
        father = row_start
        child = None
        while father and father.left:
            if child:
                child.next = father.left
                child = child.next
            else:
                child = father.left
            child.next = father.right
            child = child.next
            father = father.next
        row_start = row_start.left
    return root