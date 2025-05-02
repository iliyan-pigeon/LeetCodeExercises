from typing import List
from collections import Counter


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
      
