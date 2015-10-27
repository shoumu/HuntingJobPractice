# coding=utf-8
__author__ = 'Arthur'


def has_cycle(head):
    fore = head.next
    while fore:
        if fore == head or fore.next == head:
            return True
        head = head.next
        if fore.next:
            fore = fore.next.next
        else:
            fore = fore.next
    return False