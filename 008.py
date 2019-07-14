# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = newNode = ListNode(0)
        index = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            val = x+y+index if x+y+index <= 9 else x+y+index-10

            newNode.next = ListNode(val)
            newNode = newNode.next

            index = 0 if x+y+index <= 9 else 1

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if index == 1:
            newNode.next = ListNode(1)
            newNode = newNode.next

        return head.next
