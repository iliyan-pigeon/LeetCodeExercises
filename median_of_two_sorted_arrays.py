from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        result = None

        if len(nums1) % 2 == 0:
            first_number = nums1[len(nums1)//2]
            second_number = nums1[len(nums1)//2 - 1]

            result = (first_number + second_number) / 2
        else:
            result = nums1[len(nums1) // 2]

        return result
      
