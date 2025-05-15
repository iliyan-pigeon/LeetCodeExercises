from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []

        for i in range(1, len(nums)+1):
            if sum(nums[:i]) % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result
      
