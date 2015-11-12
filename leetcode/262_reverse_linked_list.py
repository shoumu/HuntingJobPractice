#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/12 12:22


def reverse_list(head):
    if not head:
        return head
    ne = head.next
    head.next = None
    while ne:
        tmp = ne.next
        ne.next = head
        head = ne
        ne = tmp
    return head


def reverse_list_2(head):
    if not head or not head.next:
        return head
    root = reverse_list_2(head.next)
    head.next.next = head
    head.next = None
    return root

