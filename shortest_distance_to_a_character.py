from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []

        for i, ch in enumerate(s):
            distance = 0

            if ch == c:
                result.append(distance)
                continue

            while True:
                distance += 1

                if i - distance >= 0:
                    if s[i-distance] == c:
                        result.append(distance)
                        break

                if i + distance < len(s):
                    if s[i+distance] == c:
                        result.append(distance)
                        break

        return result
      
