#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/23 16:39


def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for i in range(n)]

    def calculate(i, j):
        if dp[i][j] or i == j - 1:
            return dp[i][j]
        coins = 0
        for k in range(i + 1, j):
            coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
        dp[i][j] = coins
        return coins

    return calculate(0, n - 1)


nums = [3, 1, 5, 8]
print(max_coins(nums))
