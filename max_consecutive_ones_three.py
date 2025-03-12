from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest_run = 0
        start = 0
        zeros_count = 0

        for end in range(len(nums)+1):
            current_binary = nums[start:end]

            if len(current_binary) > longest_run:
                longest_run = len(current_binary)

            if end < len(nums):
                if nums[end] == 0:
                    zeros_count += 1

            while zeros_count > k:
                if nums[start] == 0:
                    zeros_count -= 1

                start += 1

        return longest_run


