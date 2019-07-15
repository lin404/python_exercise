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

        self.flatten(root.left)
        self.flatten(root.right)

        p = root
        if not root.left:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None

# [1,2,5,3,4,null,6]
# [1,null,2,null,3,null,4,null,5,null,6]
