from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        nodes_values = []

        for node in lists:
            while node:
                nodes_values.append(node.val)
                node = node.next

        nodes_values.sort()

        for v in nodes_values:
            current.next = ListNode(v)
            current = current.next

        return dummy.next
    