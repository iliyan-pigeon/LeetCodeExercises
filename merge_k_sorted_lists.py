from typing import Optional, List
from heapq import heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
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


# Solution 2
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap
        min_heap = []

        # Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))

        # Create a dummy node to simplify the merge logic
        dummy = ListNode()
        current = dummy

        # Merge the lists
        while min_heap:
            # Extract the smallest element from the heap
            val, i, node = heappop(min_heap)
            # Add the extracted value to the merged list
            current.next = ListNode(val)
            current = current.next

            # If the extracted node has a next node, add it to the heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
