from typing import List


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
