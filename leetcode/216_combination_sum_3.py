#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/2/17 18:14


class Solution(object):

    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.com_sum(n, [], k, 1)
        print(self.result)
        return self.result

    def com_sum(self, target, cur_list, nth, start_num):
        if nth <= 0:
            if target == 0:
                self.result.append(list(cur_list))
            return
        if start_num > 9 or target < 0:
            return
        for i in range(start_num, 10):
            if target - i >= 0:
                cur_list.append(i)
                self.com_sum(target - i, cur_list, nth - 1, i + 1)
                cur_list.pop()


if __name__ == '__main__':
    test = Solution()
    test.combinationSum3(3, 9)
