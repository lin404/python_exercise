# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        newLst = []

        head = point = ListNode(0)
        for node in lists:
            while node:
                newLst.append(node.val)
                node = node.next

        for item in sorted(newLst):
            point.next = ListNode(item)
            point = point.next

        return head.next
