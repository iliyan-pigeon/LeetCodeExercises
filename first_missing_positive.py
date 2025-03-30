from typing import List


# Solution 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(1, max(nums)+2):
            if i not in nums:
                return i
