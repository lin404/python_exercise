# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        return self.getLeafs(root1) == self.getLeafs(root2)

    def getLeafs(self, root):
        rst = []
        if not root:
            return rst

        else:
            if not root.left and not root.right:
                return [root.val]

            rst.extend(self.getLeafs(root.left))
            rst.extend(self.getLeafs(root.right))

        return rst
