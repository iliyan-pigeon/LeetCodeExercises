from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []

        for i in operations:
            current = None
            if i == "+":
                current = result[-1] + result[-2]
                result.append(current)

            elif i == "D":
                current = result[-1] * 2
                result.append(current)

            elif i == "C":
                result.pop()

            else:
                result.append(int(i))

        return sum(result)
      
