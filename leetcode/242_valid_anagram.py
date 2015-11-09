#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2015/11/9 11:10


def is_anagram(s, t):
    count = {}
    for ch in s:
        if count.get(ch, None):
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in t:
        if count.get(ch, None):
            count[ch] -= 1
            if count[ch] == 0:
                count.pop(ch)
        else:
            return False
    if not count:
        return True
    return False


def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for c in count:
        if c != 0:
            return False
    return True


s = 'anagram'
t = 'nagaram'
# s = 'rat'
# t = 'cat'
print(is_anagram_2(s, t))
