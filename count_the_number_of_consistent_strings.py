from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for word in words:
            valid = True
            for ch in word:
                if ch not in allowed:
                    valid = False
                    break

            if valid:
                result += 1

        return result
