from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1 = Counter(word1)
        word2 = Counter(word2)

        for k, v in word1.items():
            if k not in word2 and v > 3:
                return False
            elif abs(v - word2[k]) > 3:
                return False

        return True
