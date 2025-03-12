from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        start = 0
        end = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1

            if k < 0:
                if nums[start] == 0:
                    k += 1

                start += 1
        return end - start + 1
