#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/17 11:41


def generate_parentheses(n):
    """
    :param n: int
    :return: List[str]
    """
    m = []
    generate(m, '', n, n)
    return m


def generate(m, s, l, r):
    if l == 0 and r == 0:
        m.append(s)
        return
    if l > 0:
        generate(m, s + '(', l - 1, r)
    if r > l:
        generate(m, s + ')', l, r - 1)


print(generate_parentheses(3))