import sys
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = - sys.maxsize

        for i in range(len(nums) + 1 - k):
            current_sum = sum(nums[i:i+k])
            current_len = len(nums[i:i+k])
            current_average = current_sum / current_len

            if current_average > max_average:
                max_average = current_average

        return max_average
