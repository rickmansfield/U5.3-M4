"""
You are given a binary tree.
Write a function that can return the inorder traversal of node values.
Example:
Input:
   3
    \
     1
    /
   5
Output: [3,5,1]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root, results=None):
    if results == None:
        results = []
    if root is None:
        return
    inorder_traversal(root.left, results)
    results.append(root.val)
    inorder_traversal(root.right, results)

    return results


# test
n = TreeNode(3)
n.right = TreeNode(1)
n.right.left = TreeNode(5)

res = inorder_traversal(n)
print(res)
