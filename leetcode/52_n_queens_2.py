#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/5 11:59


count = 0


def total_n_queens(n):
    global count
    state = [0] * n
    queens(n, state, 0)
    return count


def queens(num, state, index):
    if index is num:
        global count
        count += 1
    else:
        for next_x in range(num):
            if not conflict(state, next_x, index):
                state[index] = next_x
                queens(num, state, index+1)


def conflict(state, next_x, next_y):
    for i in range(next_y):
        if abs(next_x - state[i]) in (0, next_y - i):
            return True
    return False


print(total_n_queens(8))

