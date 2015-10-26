# encoding:utf-8
__author__ = 'Arthur'


def reverse_bits(n):
    ans = 0
    for i in range(32):
        ans <<= 1
        ans |= n & 1
        n >>= 1
    return ans


reverse_bits(31)