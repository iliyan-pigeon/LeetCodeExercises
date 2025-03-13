from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for c in word1:
            count1[c] += 1

        for c in word2:
            count2[c] += 1

        return count1.keys() == count2.keys() and (sorted(count1.values()) == sorted(count2.values()))