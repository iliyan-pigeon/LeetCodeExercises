from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = []

        while head:
            if head in visited:
                return head

            visited.append(head)
            head = head.next

        return


# Solution 2
class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                while head != slow:
                    head, slow = head.next, slow.next
                return head
        return 
