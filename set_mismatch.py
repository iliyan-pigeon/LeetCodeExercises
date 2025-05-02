from typing import List
from collections import Counter


# Solution 1
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        result = []

        for key, value in nums_dict.items():
            if value == 2:
                result.append(key)
                for i in range(1, len(nums)+1):
                    if i not in nums:
                        result.append(i)
                        break
                break

        return result


# Solution 2
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = n * (n + 1) // 2

        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        return [duplicate, missing]
