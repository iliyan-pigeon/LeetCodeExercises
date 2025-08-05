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


# Solution 2
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev

        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next


# Solution 3
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
