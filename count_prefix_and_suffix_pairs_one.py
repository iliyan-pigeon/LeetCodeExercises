from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)):
            current = words[i]
            for j in range(i+1, len(words)):
                if words[j].startswith(current) and words[j].endswith(current):
                    pairs += 1

        return pairs
