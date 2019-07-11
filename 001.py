# Definition for a binary tree node.


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        print(f"value={self.data}")
        if self.left:
            # print(f"left={self.left}")
            self.left.printTree()
        else:
            print(f"left=None")

        if self.right:
            # print(f"right={self.right}")
            self.right.printTree()
        else:
            print(f"right=None")


# Use the insert method to add nodes
tree = Node(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.printTree()


class Solution():
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


sol = Solution()
num = sol.maxDepth(tree)
print(num)
