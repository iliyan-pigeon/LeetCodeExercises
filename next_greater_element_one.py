from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for number in nums1:
            index = nums2.index(number) + 1
            next_bigger = -1

            while index < len(nums2):
                if nums2[index] > number:
                    next_bigger = nums2[index]
                    break

            result.append(next_bigger)

        return result
      
