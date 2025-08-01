from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = ""

        while head:
            binary += str(head.val)
            head = head.next

        return int(binary, 2)
    