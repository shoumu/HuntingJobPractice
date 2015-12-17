#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/12/17 16:35


def gray_code(n):
    res = [0]
    for i in range(n):
        for j in range(len(res) - 1, -1, -1):
            res.append(1 << i | res[j])
    return res


print(gray_code(2))
