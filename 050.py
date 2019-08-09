# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def levelOrderBottom_DFS(self, root):

        def levelOrder(rst, root, level):

            if not root:
                return

            if level >= len(rst):
                rst.append([])

            rst[level].append(root.val)

            levelOrder(rst, root.left, level+1)
            levelOrder(rst, root.right, level+1)

        rst = []
        levelOrder(rst, root, 0)
        return rst[::-1]

    def levelOrderBottom_BFS(self, root):

        if not root:
            return []

        rst = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            lst = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                if not node:
                    continue

                lst.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            if lst:
                rst.append(lst)

        return rst[::-1]
