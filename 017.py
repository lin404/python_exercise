# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        right = root.right
        left = root.left
        root.left = None

        self.flatten(left)
        self.flatten(right)

        root.right = left

        while root.right:
            root = root.right

        root.right = right

# [1,2,5,3,4,null,6]
# [1,null,2,null,3,null,4,null,5,null,6]
