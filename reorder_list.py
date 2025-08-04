from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_nodes = []
        middle = slow.next

        while slow.next:
            second_nodes.append(slow.next)
            slow = slow.next

        current = head.next
        dummy = ListNode()
        dummy.next = head

        while current != middle and second_nodes:
            head.next = second_nodes.pop()
            head = head.next
            head.next = current
            head = head.next
            current = current.next

        return dummy.next