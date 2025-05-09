from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        difference = max(nums) - min(nums)

        if difference <= k*2:
            return 0

        return difference + k*2
      
