from typing import List


# Solution 1
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set(nums1) & set(nums2)
        return list(intersection)


# Solution 2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for number in nums1:
            if number in nums2:
                result.append(number)

        for number in nums2:
            if number in nums1 and number not in result:
                result.append(number)

        return result
      
