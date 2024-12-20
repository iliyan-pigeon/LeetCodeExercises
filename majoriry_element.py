class Solution(object):
    def majorityElement(self, nums):
    
        elements = set(nums)
    
        for element in elements:
            count = nums.count(element)
    
            if count > len(nums) / 2:
                return element
