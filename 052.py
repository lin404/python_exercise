"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder_BFS(self, root):

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
                queue.extend([child for child in node.children])

            if lst:
                rst.append(lst)

        return rst
