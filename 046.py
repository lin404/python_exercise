# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):

        def mirror(left, right):
            if not left or not right:
                return left == right

            elif left.val != right.val:
                return False

            return mirror(left.left, right.right) and mirror(left.right, right.left)

        if not root:
            return True

        return mirror(root.left, root.right)

    def isSymmetric_DFS(self, root):

        if not root:
            return True

        stackl, stackr = [root.left], [root.right]
        while len(stackl) > 0 and len(stackr) > 0:
            left = stackl.pop()
            right = stackr.pop()

            if not left and not right:
                continue
            elif not left or not right:
                return False

            if left.val != right.val:
                return False

            stackl.append(left.left)
            stackl.append(left.right)
            stackr.append(right.right)
            stackr.append(right.left)

        return len(stackl) == len(stackr)
