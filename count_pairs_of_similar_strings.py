from collections import Counter
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        result = 0

        uniques = []

        words = ["".join(sorted(set(i))) for i in words]
        words = Counter(words)

        for v in words.values():
            result += v * (v - 1) // 2

        return result
