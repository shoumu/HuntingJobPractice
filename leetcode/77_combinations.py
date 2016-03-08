#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/8 12:41


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.combines = []
        self.combine_one([], n, k, 1, 1)
        return self.combines

    def combine_one(self, cur_list, n, k, num_index, start_index):
        if num_index == k + 1:
            self.combines.append(list(cur_list))
            return
        if n - start_index < k - num_index:
            return
        for i in range(start_index, n + 1):
            self.combine_one(cur_list + [i], n, k, num_index + 1, i + 1)


solution = Solution()
tmp = solution.combine(10, 8)
print(tmp)
