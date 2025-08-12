from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        nodes_values = []

        while head:
            nodes_values.append(head.val)
            head = head.next

        nums = sorted(nums, key=lambda x: {num: i for i, num in enumerate(nodes_values)}.get(x, len(nodes_values)))
        connected = 1
        previous = nums[0]
        for index in range(1, len(nums)):
            if abs(nodes_values.index(nums[index]) - nodes_values.index(previous)) > 1:
                connected += 1
            previous = nums[index]

        return connected
