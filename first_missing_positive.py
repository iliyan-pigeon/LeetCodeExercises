from typing import List


# Solution 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1

        for num in nums:
            if num == smallest:
                smallest += 1

        return smallest


# Solution 2
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        smallest = 1

        while smallest in num_set:
            smallest += 1

        return smallest
