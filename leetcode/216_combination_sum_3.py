#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/17 18:14


def combination_sum_3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    result = []
    combination = []
    for i in range(1, 11 - k):
        if i > n:
            break
        combination.append(i)
        tmp = i
        sum = i
        for j in range(k):
            for p in range(tmp + 1, 10):
                if sum + p > n:


combination_sum_3(3, 1)
