from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, number in enumerate(nums):
            if k == 0:
                break

            if number < 0:
                nums[i] = abs(number)
                k -= 1

            else:
                while k:
                    if number < 0:
                        nums[i] = abs(number)
                    else:
                        nums[i] = -number

                    k -= 1

        return sum(nums)
      
