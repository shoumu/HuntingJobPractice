#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/16 15:39


def unique_paths(m, n):
    """
    according to the Combinatorics, the result is C(m - 1)(m + n -2)
    :param m:
    :param n:
    :return:
    """
    a = m + n - 2
    b = m - 1
    result = 1
    for i in range(b):
        result *= a
        a -= 1
    for i in range(1, b + 1):
        result /= i
    return int(result)


def unique_paths_2(m, n):
    """
    a dynamic programming solution
    the formula is f(m, n) = f(m - 1, n) + f(m, n - 1)
    :param m:
    :param n:
    :return:
    """
    matrix = [[1] * n] * m
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] = matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[m - 1][n - 1]


print(unique_paths_2(2, 2))
print(unique_paths_2(3, 2))
print(unique_paths_2(1, 10))
print(unique_paths_2(10, 1))
