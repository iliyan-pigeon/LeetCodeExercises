from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [i for i in set(nums)]
        nums.sort(reverse=True)

        if len(nums) < 3:
            return nums[0]
        return nums[2]
      
