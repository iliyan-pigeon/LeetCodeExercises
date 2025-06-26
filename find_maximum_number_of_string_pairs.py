from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pairs = 0

        for ch in words:
            if ch[::-1] in words:
                pairs += 1

        return pairs // 2
