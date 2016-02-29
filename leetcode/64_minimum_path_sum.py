#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/25 9:50


def min_path_sum(grid):
    if not grid:
        return 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            left = 99999999
            up = 99999999
            if i:
                left = grid[i - 1][j]
            if j:
                up = grid[i][j - 1]
            grid[i][j] += min(left, up)
    return grid[m - 1][n - 1]


grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
grid = [[1, 1, 1]]
grid = [[1, 1], [1, 1]]
grid = []
print(min_path_sum(grid))
