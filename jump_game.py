# Solution 1
from typing import List


class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return False


# Solution 2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        answers = [False] * length

        for i in range(len(nums)-1, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j >= length-1:
                    answers[i] = True
                    break
                elif answers[i+j] is True:
                    answers[i] = True
                    break

        return answers[0]
