#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/25 11:09


def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    i = j = 0
    num = 1
    start_index = 0
    max_num = n * n
    while num <= max_num:
        while j < n:
            matrix[i][j] = num
            num += 1
            j += 1
        j -= 1
        i += 1
        while i < n:
            matrix[i][j] = num
            num += 1
            i += 1
        i -= 1
        j -= 1
        while j >= start_index:
            matrix[i][j] = num
            num += 1
            j -= 1
        j += 1
        i -= 1
        while i > start_index:
            matrix[i][j] = num
            num += 1
            i -= 1
        start_index += 1
        i = j = start_index
        n -= 1

    def print_matrix():
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end='\t')
            print()

    print_matrix()
    return matrix


generate_matrix(2)
