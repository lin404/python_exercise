class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def depth(self, root):
        if not root:
            return 0
        rst = max(self.depth(root.left), self.depth(root.right))+1
        print(rst)
        return rst

    def isBalanced(self, root):
        if not root:
            return True

        l = self.depth(root.left)
        r = self.depth(root.right)
        if abs(r-l) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
