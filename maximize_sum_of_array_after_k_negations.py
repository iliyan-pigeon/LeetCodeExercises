from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        negatives_count = len([i for i in nums if i < 0])

        for i, number in enumerate(nums):
            if k == 0:
                break

            if number < 0:
                if negatives_count == 1 and k % 2 != 0:
                    nums[i] = abs(number)
                    k = 0
                else:
                    if i < len(nums)-1 and negatives_count == 1:
                        if abs(number) < nums[i+1]:
                            k = 0
                    else:
                        nums[i] = abs(number)
                        k -= 1
                        negatives_count -= 1

            else:
                while k:
                    if number < 0:
                        nums[i] = abs(number)
                    else:
                        nums[i] = -number

                    k -= 1

        return sum(nums)
        
