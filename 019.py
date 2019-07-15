class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        head = pre
        return head
