from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            current = word[:i]+word[i+1:]

            if set([i for i in Counter(current).values()]) == 1:
                return True

        return False
