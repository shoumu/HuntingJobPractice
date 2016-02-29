#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 16/2/29 23:07


def max_area(height):
    area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        h = min(height[i], height[j])
        w = j - i
        area = max(area, h * w)
        while i < j and height[i] <= h:
            i += 1
        while i < j and height[j] <= h:
            j -= 1
    return area


test_height = [1, 2, 3, 4]
print(max_area(test_height))
