#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/2 16:13


def game_of_life(board):
    m = len(board)
    n = len(board[0])

    def live_neighbors(i, j):
        nei_lives = 0
        for x in range(max(i - 1, 0), min(i + 2, m)):
            for y in range(max(j - 1, 0), min(j + 2, n)):
                nei_lives += board[x][y] & 1
        nei_lives -= board[i][j] & 1
        return nei_lives

    for i in range(m):
        for j in range(n):
            lives = live_neighbors(i, j)
            if board[i][j] == 1 and 2 <= lives <= 3:
                board[i][j] = 3
            if board[i][j] == 0 and lives == 3:
                board[i][j] = 2
    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1


test_board = [[1]]
game_of_life(test_board)
print(test_board)