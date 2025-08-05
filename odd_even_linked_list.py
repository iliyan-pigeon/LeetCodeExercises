from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_odd = ListNode()
        dummy_even = ListNode()
        current_odd = dummy_odd
        current_even = dummy_even

        odd = True

        while head:
            if odd:
                current_odd.next = ListNode(head.val)
                current_odd = current_odd.next
                odd = False
            else:
                current_even.next = ListNode(head.val)
                current_even = current_even.next
                odd = True

            head = head.next

        current_odd.next = dummy_even.next

        return dummy_odd.next
    