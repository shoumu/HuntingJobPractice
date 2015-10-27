# coding:utf-8
__author__ = 'Arthur'


def single_number(a):
    temp = 0
    for n in a:
        temp ^= n
    return temp


print(single_number([1, 1, 2]))