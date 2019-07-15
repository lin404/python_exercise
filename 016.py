# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElementsSimpler(self, head, val):
        if not head:
            return head

        head.next = self.removeElementsSimpler(head.next, val)
        return head if head.val != val else head.next

    def removeElements(self, head, val):

        if not head:
            return head

        slow = node = ListNode(0)
        while head:

            if head.val == val:
                slow.next = head.next
            else:
                slow = slow.next

            head = head.next

        return node.next

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
