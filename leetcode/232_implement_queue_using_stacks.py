#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/1/5 14:11


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        temp.pop()
        self.stack = temp
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        self.stack = temp

    def peek(self):
        """
        :rtype: int
        """
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        res = temp[len(temp) - 1]
        self.stack = temp
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        self.stack = temp
        return res

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        return True


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
print(queue.peek())
print(queue.empty())
