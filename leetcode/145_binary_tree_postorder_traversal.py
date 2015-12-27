#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 15/12/27 22:04


def postorder_traversal(root):
    if not root:
        return []
    stack = [root]
    res = []
    pre = None
    while stack:
        cur = stack.pop()
        if (cur.left is None and cur.right is None) or (pre and (cur.left is pre or cur.right is pre)):
            res.append(cur.val)
            pre = cur
        else:
            stack.append(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
    return res
