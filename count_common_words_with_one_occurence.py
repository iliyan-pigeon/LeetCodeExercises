from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = Counter(words1)
        words2 = Counter(words2)

        result = 0

        for k, v in words1.items():
            if v == 1 and k in words2:
                if words2[k] == 1:
                    result += 1

        return result
