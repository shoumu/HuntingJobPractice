# coding=utf-8
__author__ = 'Arthur'


def title_to_number(s):
    num = 0
    for ch in s:
        num *= 26
        num += (ord(ch) - ord('A') + 1)
    return num


print(title_to_number('AA'))