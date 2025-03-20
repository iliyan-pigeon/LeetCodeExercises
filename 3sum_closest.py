import sys
from typing import List


# Solution 1 (A bit slow)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = None
        distance = sys.maxsize

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    current_sum = sum([nums[i], nums[j], nums[k]])
                    current_distance = None

                    if current_sum > target:
                        current_distance = current_sum - target
                    elif current_sum < target:
                        current_distance = target - current_sum
                    elif current_sum == target:
                        return current_sum

                    if current_distance < distance:
                        distance = current_distance
                        closest_sum = current_sum

        return closest_sum
