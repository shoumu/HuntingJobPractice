# coding=utf-8
__author__ = 'Arthur'


def num_of_bst(n):
    count = [1, 1]
    for i in range(2, n + 1):
        count.append(0)
        for j in range(0, i):
            count[i] += count[j] * count[i - 1 - j]
    return count[n]


print(num_of_bst(3))