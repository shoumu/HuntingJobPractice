#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: shoumuzyq@gmail.com
#         https://shoumu.github.io
# Created on 2016/3/9 10:42


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.symmetric_compare(root.left, root.right)
        return True

    def symmetric_compare(self, node1, node2):
        if node1 and node2 and node1.val == node2.val:
            return self.symmetric_compare(node1.left, node2.right) and self.symmetric_compare(node1.right, node2.left)
        elif not node1 and not node2:
            return True
        else:
            return False

    def isSymmetric2(self, root):
        if not root:
            return True
        left = [root.left]
        right = [root.right]
        while left and right:
            node1 = left.pop(0)
            node2 = right.pop(0)
            if node1 and node2 and node1.val == node2.val:
                left.append(node1.left)
                left.append(node1.right)
                right.append(node2.right)
                right.append(node2.left)
            elif not node1 and not node2:
                continue
            else:
                return False
        return len(left) == 0 and len(right) == 0



node1 = TreeNode(1)
node21 = TreeNode(2)
node22 = TreeNode(2)
node31 = TreeNode(3)
node32 = TreeNode(3)
node41 = TreeNode(4)
node42 = TreeNode(4)

node1.left = node21
node1.right = node22
node21.left = node31
node21.right = node41
node22.left = node42
node22.right = node32

solution = Solution()
print(solution.isSymmetric2(node1))
