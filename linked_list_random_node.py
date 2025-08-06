import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.nodes_values = []
        while head:
            self.nodes_values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.nodes_values[random.randint(0, len(self.nodes_values)-1)]
    