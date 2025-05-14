from typing import List


class Solution:
    def sortedSquared(self, nums: List[int]) -> List[int]:
        nums = [n ** 2 for n in nums]
        nums.sort()

        return nums
      
