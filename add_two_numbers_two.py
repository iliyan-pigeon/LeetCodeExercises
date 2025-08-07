from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = ""
        l2_string = ""

        while l1:
            l1_string += str(l1.val)
            l1 = l1.next

        while l2:
            l2_string += str(l2.val)
            l2 = l2.next

        result = int(l1_string) + int(l2_string)

        dummy = ListNode()
        current = dummy

        for ch in str(result):
            node = ListNode(int(ch))
            current.next = node
            current = current.next

        return dummy.next
    