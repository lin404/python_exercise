"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def maxDepth_DFS(self, root):
        if not root:
            return 0
        if not root.children:
            return 1

        depth = 1 + max(self.maxDepth_DFS(child) for child in root.children)
        return depth

    def maxDepth_BFS(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            depth += 1

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                queue.extend([child for child in node.children])

        return depth
