from typing import List

from collections import defaultdict


# Solution 1

class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []

        for number in set(nums1):

            if number in nums2:

                times = min(nums1.count(number), nums2.count(number))

                for i in range(times):
                    result.append(number)

        return result


# Solution 2

class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter = defaultdict(int)

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        for i in nums1:
            counter[i] += 1

        result = []

        for i in nums2:

            counts = counter[i]

            if counts > 0:
                result.append(i)

                counter[i] -= 1

        return result