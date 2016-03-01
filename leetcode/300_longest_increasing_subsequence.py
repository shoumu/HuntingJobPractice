#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/1 10:22


import bisect


# the complexity of the this algorithm is O(n^2)
def length_of_lis(nums):
    length_list = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and length_list[i] < length_list[j] + 1:
                length_list[i] = length_list[j] + 1
    if length_list:
        return max(length_list)
    else:
        return 0


# https://leetcode.com/discuss/82155/share-my-8-line-o-nlgn-java-code-with-comments-in-mandarin
# cap[i] store the minimum value of the last element of list which length is i + 1
def length_of_lis_2(nums):
    cap = []
    for num in nums:
        if not cap or num > cap[len(cap) - 1]:
            cap.append(num)
        else:
            index = bisect.bisect_left(cap, num)
            cap[index] = num
    return len(cap)


test_nums = [10, 9, 2, 5, 3, 7, 101, 18]
test_nums = [2, 2]
test_nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
print(length_of_lis_2(test_nums))

