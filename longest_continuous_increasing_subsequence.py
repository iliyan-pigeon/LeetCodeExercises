from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        current_result = 0

        for i in range(len(nums)):
            if current_result == 0:
                current_result += 1
                continue

            if nums[i] > nums[i-1]:
                current_result += 1
                if current_result > result:
                    result = current_result
            else:
                if current_result > result:
                    result = current_result
                current_result = 1

        return result
      
