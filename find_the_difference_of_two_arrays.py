from typing import List


# Solution 1
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


# Solution 2
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = list(set1-set2)
        list2 = list(set2-set1)

        return [list1, list2]


# Solution 3
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [[*(set1 - set2)], [*(set2 - set1)]]
