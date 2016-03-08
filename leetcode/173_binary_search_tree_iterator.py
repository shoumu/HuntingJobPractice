#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/8 10:01

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.pre = None
        self.tree = []
        if root:
            self.tree.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        # if not (self.root and self.tree):
        if self.root and self.tree:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        tmp = self.tree.pop()
        if not tmp.left or tmp.left == self.pre or (self.pre and self.pre.val > tmp.left.val):
            if tmp.right:
                self.tree.append(tmp.right)
            self.pre = tmp
            return tmp.val
        else:
            while tmp and tmp.left:
                self.tree.append(tmp)
                tmp = tmp.left
            if tmp.right:
                self.tree.append(tmp.right)
            self.pre = tmp
            return tmp.val


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# node2.left = node1
# node2.right = node3
# node4.left = node2
# node4.right = node5

node3.left = node1
node3.right = node4
node1.right = node2

# Your BSTIterator will be called like this:
i, v = BSTIterator(node3), []
while i.hasNext():
    v.append(i.next())
print(v)
