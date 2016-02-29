#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 16/2/29 22:03


def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]
            matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]
            matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end='\t')
        print()


matrix = [[1, 2], [3, 4]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = []
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print_matrix(matrix)
rotate(matrix)
print_matrix(matrix)
