from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next


# Solution 2
class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = set()

        dummy = ListNode()
        dummy.next = head
        current = dummy.next

        while current:
            values.add(current.val)
            current = current.next

        values = sorted([i for i in values])

        if len(values) == 1:
            head = ListNode(values[0])
            return head

        for i in range(1, len(values)):
            head.next = ListNode(values[i])
            head = head.next

        return dummy.next