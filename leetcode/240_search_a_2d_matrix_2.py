#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/1 11:53


def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix:
        return search(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
    else:
        return False


def search(matrix, target, ms, me, ns, ne):
    if ms < 0 or me >= len(matrix) or ns < 0 or ne >= len(matrix[0]) or ms > me or ns > ne:
        return False
    mm = (ms + me) // 2
    nm = (ns + ne) // 2
    if ms > me or ns > ne:
        return False
    if matrix[mm][nm] == target:
        return True
    elif matrix[mm][nm] > target:
        return search(matrix, target, ms, mm - 1, ns, nm - 1) \
               or search(matrix, target, mm, me, ns, nm - 1) \
               or search(matrix, target, ms, mm - 1, nm, ne)
    else:
        return search(matrix, target, mm + 1, me, nm + 1, ne) \
               or search(matrix, target, mm + 1, me, ns, nm) \
               or search(matrix, target, ms, mm, nm + 1, ne)


test_matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
test_matrix = []
test_matrix = [[-5]]
test_matrix = [[1, 1]]

print(search_matrix(test_matrix, 1))
