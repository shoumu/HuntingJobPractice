#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/27 11:26


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

