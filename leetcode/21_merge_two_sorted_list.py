#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/28 12:27


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_list(l1, l2):
    if l1 and not l2:
        return l1
    if l2 and not l1:
        return l2
    if not l1 and not l2:
        return None
    if l1.val <= l2.val:
        rlh = l1
        l1 = l1.next
    else:
        rlh = l2
        l2 = l2.next
    cur = rlh
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return rlh


def merge_two_list_2(l1, l2):
    tmp = ListNode(-1)
    cur = tmp
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            cur = cur .next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return tmp.next


l1 = ListNode(5)
l2 = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(4)
l2.next = node1
node1.next = node2

res = merge_two_list_2(l1, l2)
while res:
    print(res.val)
    res = res.next
