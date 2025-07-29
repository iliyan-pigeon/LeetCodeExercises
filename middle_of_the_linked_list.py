from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_amount = 0
        current = head

        while current:
            nodes_amount += 1
            current = current.next

        current_node = 1

        while current_node*2 <= nodes_amount:
            current_node += 1
            head = head.next

        print(head.val)
        return head
    