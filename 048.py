# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, sum):

        if not root:
            return 0

        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
