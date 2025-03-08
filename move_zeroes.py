from typing import List


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


a = Solution()
print(a.moveZeroes([0,1,0,3,12]))
