__author__ = 'Arthur'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def inorder_traversal(root):
    out = []
    visited = []
    if root:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.right and cur.right not in stack:
                stack.append(cur.right)
            if not cur.left or cur.left in visited:
                out.append(cur.val)
                visited.append(cur)
            else:
                stack.append(cur)
                if cur.left:
                    stack.append(cur.left)
    return out


# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node1.right = node2
# node2.left = node3

node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(2)
node1.left = node2
node1.right = node3

root = node1
print(inorder_traversal(node1))