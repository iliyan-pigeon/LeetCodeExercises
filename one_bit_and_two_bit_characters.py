from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pointer = 0
        result = False

        while pointer < len(bits):
            if bits[pointer] == 1:
                pointer += 2
                result = False
            elif bits[pointer] == 0:
                pointer += 1
                result = True
                
        return result
      
