from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set([i for i in Counter(s).values()])) == 1
