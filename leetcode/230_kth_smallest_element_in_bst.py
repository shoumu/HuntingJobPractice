#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/18 13:14


def kth_smallest(root, k):
    num = 0
    node_stack = []
    cur = root
    while cur or node_stack:
        while cur:
            node_stack.append(cur)
            cur = cur.left
        cur = node_stack.pop()
        num += 1
        if num is k:
            return cur.val
        cur = cur.right