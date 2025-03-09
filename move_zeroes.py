from typing import List

# Solution 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        while True:
            should_break = False

            for i in range(len(nums)):
                if nums[i:].count(0) == len(nums[i:]):
                    should_break = True
                    break

                if nums[i] == 0:
                    nums.pop(i)
                    nums.append(0)
                    break

            if should_break:
                break


# Solution 2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
