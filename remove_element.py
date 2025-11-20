from typing import List


class Solution(object):
    def removeElement(self, nums, val):
        
        while val in nums:
            nums.remove(val)

        return len(nums)


# Solution 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        for i in range(len(nums)):
            if nums[i-removed] == val:
                nums.pop(i-removed)
                removed += 1
