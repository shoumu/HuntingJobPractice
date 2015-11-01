#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/1 14:27


def product_except_self(nums):
    product = 1
    zero_count = 0
    out = []
    for num in nums:
        product *= num
        if num is 0:
            zero_count += 1
    if zero_count >= 2:
        out = [0] * len(nums)
    elif zero_count == 1:
        for num in nums:
            if num != 0:
                out.append(0)
            else:
                tmp = 1
                for t in nums:
                    if t != 0:
                        tmp *= t
                out.append(tmp)
    else:
        for num in nums:
            out.append(int(product / num))
    return out


def product_except_self_2(nums):
    """
    from the two direction to product
    :param nums:
    :return: List<int>
    """
    out = [0] * len(nums)
    product = 1
    for i in range(len(nums)):
        out[i] = product
        product *= nums[i]
    product = 1
    for i in range(len(nums))[::-1]:
        out[i] *= product
        product *= nums[i]
    return out


nums = [1, 2, 3, 4]
nums = [0, 1, 2, 3]
# nums = [0, 0, 1, 2]
print(product_except_self(nums))
print(product_except_self_2(nums))
