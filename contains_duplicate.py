from typing import List


# Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False


# Solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        collected = {}

        for number in nums:
            if number not in collected:
                collected[number] = 0
            collected[number] += 1

            if collected[number] == 2:
                return True

        return False


# Solution 3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for number in nums:
            if nums.count(number) > 1:
                return True

        return False
      
