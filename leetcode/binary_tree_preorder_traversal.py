# coding=utf-8
__author__ = 'Arthur'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def preorder_traversal(root):
    outlist = []
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            outlist.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return outlist


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3

temp = preorder_traversal(node1)
print(temp)