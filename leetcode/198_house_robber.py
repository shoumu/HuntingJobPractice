#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/9 11:08


import datetime


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            money = [0] * len(nums)
            money[0] = nums[0]
            money[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                money[i] = max(money[i - 1], money[i - 2] + nums[i])
            return money[len(nums) - 1]

    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            first = nums[0]
            second = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                second, first = max(second, first + nums[i]), second
            return second


nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
        185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solution = Solution()
start = datetime.datetime.now()
print(solution.rob(nums))
print(int((datetime.datetime.now() - start).total_seconds() * 1000))
