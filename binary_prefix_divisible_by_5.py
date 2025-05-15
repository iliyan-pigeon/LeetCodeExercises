from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_value = ""

        for bit in nums:
            current_value += str(bit)

            if int(current_value, 2) % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result
        
