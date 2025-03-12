from typing import List


# Solution 1
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


# Solution 2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
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
