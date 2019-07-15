class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEndSimpler(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy

        for _ in range(n+1):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        pre = head
        count = 0

        while pre:
            count += 1
            pre = pre.next

        node = pre = ListNode(0)
        pre.next = head
        while count > 0:
            if count == n:
                pre.next = head.next
            else:
                pre = pre.next

            head = head.next
            count -= 1

        return node.next
