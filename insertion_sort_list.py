from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        dummy = ListNode()
        current = dummy

        while head:
            if dummy.next is None:
                next_one = ListNode(head.val)
                dummy.next = next_one
                head = head.next

            while current.next:
                if head.val < current.next.val:
                    move = current.next
                    next_one = ListNode(head.val)
                    current.next = next_one
                    current = current.next
                    current.next = move
                    break

                current = current.next
            if current.next is None:
                next_one = ListNode(head.val)
                current.next = next_one

            current = dummy
            head = head.next

        return dummy.next
    