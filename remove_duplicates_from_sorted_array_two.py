from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if nums.count(nums[i]) > 2:
                nums.pop(i)


# Solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 2

        while pointer < len(nums):
            if nums[pointer-1] == nums[pointer] and nums[pointer-2] == nums[pointer]:
                nums.pop(pointer)
            else:
                pointer += 1

        return len(nums)


# Solution 3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        controller = {}
        removed = 0

        for i in range(len(nums)):
            if nums[i-removed] not in controller:
                controller[nums[i-removed]] = 1
            elif controller[nums[i-removed]] == 2:
                nums.pop(i-removed)
                removed += 1
            else:
                controller[nums[i-removed]] += 1
