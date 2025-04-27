from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for number in set(nums1):
            if number in nums2:
                times = min(nums1.count(number), nums2.count(number))

                for i in range(times):
                    result.append(number)

        return result
    