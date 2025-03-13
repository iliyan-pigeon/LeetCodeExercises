from collections import defaultdict


# Solution 1
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


# Solution 2
from collections import Counter


class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values())
