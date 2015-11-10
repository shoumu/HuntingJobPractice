#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/10 15:17


def roman_to_int(s):
    code = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and code[s[i]] < code[s[i + 1]] :
            result -= code[s[i]]
        else:
            result += code[s[i]]
    return result


s = 'MMMCMXCIX'
print(roman_to_int(s))
