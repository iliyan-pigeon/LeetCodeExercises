from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        current = f"{s[0]}"

        for i in range(1, len(s)):
            if i % k == 0:
                result.append(current)
                current = ""

            current += s[i]

        if len(current) < 3:
            current = f"{current}{fill}"

        result.append(current)

        return result
