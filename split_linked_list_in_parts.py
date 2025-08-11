from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        nodes_count = 0
        current = head
        while current:
            nodes_count += 1
            current = current.next

        group_size = nodes_count // k
        left_overs = nodes_count % k

        parts = []
        current = head

        for _ in range(k):
            if not current:
                parts.append(None)
                continue

            part_head = current
            size = group_size + (1 if left_overs > 0 else 0)
            if left_overs > 0:
                left_overs -= 1

            for _ in range(size - 1):
                current = current.next

            next_node = current.next
            current.next = None
            current = next_node

            parts.append(part_head)

        return parts
    