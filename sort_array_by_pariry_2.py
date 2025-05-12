from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        reordered = []
        even = 0
        odd = 1

        for i in nums:
            if i % 2 == 0:
                reordered.insert(even, i)
                even += 2
            else:
                reordered.insert(odd, i)
                odd += 2

        return reordered
