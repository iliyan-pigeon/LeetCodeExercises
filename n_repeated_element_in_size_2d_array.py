from typing import List


# Solution 1
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        for num in nums:
            if nums.count(num) >= 2:
                return num


# Solution 2
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num

            nums_set.add(num)
