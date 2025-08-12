from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        pos = {}
        i = 0
        current = head
        while current:
            pos[current.val] = i
            current = current.next
            i += 1

        nums.sort(key=lambda x: pos[x])

        connected = 1
        for index in range(1, len(nums)):
            if pos[nums[index]] - pos[nums[index - 1]] > 1:
                connected += 1

        return connected
