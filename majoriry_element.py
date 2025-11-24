from typing import List
from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
    
        elements = set(nums)
    
        for element in elements:
            count = nums.count(element)
    
            if count > len(nums) / 2:
                return element

# Solution 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        for element in set(nums):
            if nums.count(element) > len(nums) / 2:
                return element


# Solution 3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for value, count in counts.items():
            if count >= len(nums) / 2:
                return value
