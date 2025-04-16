from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        current_digit = digits[-1]
        counter = 1

        while current_digit > 9:
            digits[-counter] = 0
            if counter == len(digits):
                digits.insert(0, 1)
                break
            counter += 1
            digits[-counter] += 1
            current_digit = digits[-counter]

        return digits
      
