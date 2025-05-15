from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        current_value = 0

        for bit in A:

            print(bit)
            print(current_value << 1)

            current_value = (current_value << 1) | bit

            if current_value % 5 == 0:
                result.append(True)
            else:
                result.append(False)

        return result
        
