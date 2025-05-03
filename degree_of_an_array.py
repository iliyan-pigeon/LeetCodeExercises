import sys
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_dict = {}
        highest_frequency = 0

        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = [0, []]
            nums_dict[nums[i]][0] += 1
            nums_dict[nums[i]][1].append(i)

            if nums_dict[nums[i]][0] > highest_frequency:
                highest_frequency = nums_dict[nums[i]][0]

        smallest_range = sys.maxsize

        for i in nums_dict:
            if nums_dict[i][0] == highest_frequency:
                current_range = nums_dict[i][1][-1] - nums_dict[i][1][0] + 1

                if current_range < smallest_range:
                    smallest_range = current_range

        return smallest_range
    