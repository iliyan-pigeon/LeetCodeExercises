from typing import List


# Solution 1
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        while k:
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
                        if i == len(nums) - 2 and negatives_count == 1:
                            if abs(number) < nums[i + 1]:
                                k = 0
                            else:
                                nums[i] = abs(number)
                                k -= 1
                                negatives_count -= 1
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


# Solution 2
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k > 0 > nums[i]:
                nums[i] = -nums[i]
                k -= 1

        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)
