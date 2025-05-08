from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        banknotes = {5: 0, 10: 0, 20: 0}
        result = True

        for bill in bills:
            if bill == 5:
                banknotes[5] += 1

            elif bill == 10:
                if banknotes[5] == 0:
                    result = False
                    break

                banknotes[5] -= 1
                banknotes[10] += 1

            elif bill == 20:
                if banknotes[10] == 0 and banknotes[5] < 3:
                    result = False
                    break

                if banknotes[10] > 0 and banknotes[5] == 0:
                    result = False
                    break

                banknotes[20] += 1
                banknotes[5] -= 1

                if banknotes[10] > 0:
                    banknotes[10] -= 1
                    continue

                banknotes[5] -= 2

        return result
      
