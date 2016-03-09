#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/9 14:50


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target <= matrix[i][n - 1]:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                break
        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            x = mid // n
            y = mid % n
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


test_matrix = [[1, 1]]
test_target = 0
solution = Solution()
print(solution.searchMatrix2(test_matrix, test_target))
