from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        result = [[], []]

        for integer in nums1:
            if integer not in nums2 and integer not in result[0]:
                result[0].append(integer)

        for integer in nums2:
            if integer not in nums1 and integer not in result[1]:
                result[1].append(integer)

        return result
