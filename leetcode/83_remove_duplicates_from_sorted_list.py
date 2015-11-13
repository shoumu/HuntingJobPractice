#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/13 10:42


def delete_duplicates(head):
    temp = head
    while temp and temp.next:
        while temp.next and temp.val == temp.next.val:
            temp.next = temp.next.next
        temp = temp.next
    return head


def delete_duplicates_2(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head
