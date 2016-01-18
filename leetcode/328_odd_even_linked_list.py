#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/1/18 10:15


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def odd_even_list(head):
    odd = head
    even = None
    if odd:
        even = odd.next

    while odd and even and even.next:
        tmp = even.next
        even.next = even.next.next
        even = even.next
        tmp.next = odd.next
        odd.next = tmp
        odd = tmp

    return head


head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

tmp = odd_even_list(head)
while tmp:
    print(tmp.value)
    tmp = tmp.next

