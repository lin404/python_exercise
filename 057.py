# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root):
        d = collections.defaultdict(list)
        ans = []

        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            level = max(left, right)
            d[level].append(root.val)
            return level+1

        traverse(root)
        for i in range(len(d)):
            ans.append(d[i])
        return ans
