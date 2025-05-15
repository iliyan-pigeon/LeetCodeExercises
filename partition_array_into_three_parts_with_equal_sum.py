from typing import List


class Solution:
    def canThreePartsEquaSum(self, arr: List[int]) -> bool:

        first_pointer = 0
        second_pointer = len(arr)

        result = False

        while first_pointer < second_pointer:
            first = sum(arr[:first_pointer])
            second = sum(arr[first_pointer:second_pointer])
            third = sum(arr[second_pointer:])

            if first == second == third:
                result = True
                break

            if first > third:
                second_pointer -= 1
            else:
                first_pointer += 1

        return result
      
