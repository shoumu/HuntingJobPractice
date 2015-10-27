#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/10/27 10:46


def win_nim(n):
    if n % 4 is 0:
        return False
    else:
        return True


print(win_nim(4))
print(win_nim(5))
