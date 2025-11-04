from typing import List


class Solution(object):
    def removeDuplicates(self, nums):

        while True:
            control = []

            for i in nums:
                if i in control:
                    nums.remove(i)
                    break
                else:
                    control.append(i)

            if len(control) == len(nums):
                break

        return len(nums)        


# Solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1

        while pointer < len(nums):
            if nums[pointer - 1] == nums[pointer]:
                nums.pop(pointer)
            else:
                pointer += 1

        return len(nums)
