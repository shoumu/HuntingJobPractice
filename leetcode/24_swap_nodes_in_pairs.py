#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/17 12:13


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head):
    start_head = ListNode(0)
    start_head.next = head
    tmp = start_head
    while tmp.next and tmp.next.next:
        first = tmp.next
        second = tmp.next.next
        first.next = second.next
        second.next = first
        tmp.next = second
        tmp = first
    return start_head.next