from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        amounts = Counter(word)

        unique_amounts = []

        for v in amounts.values():
            if v not in unique_amounts:
                unique_amounts.append(v)

        if len(unique_amounts) == 2:
            if abs(unique_amounts[0] - unique_amounts[1]) == 1:
                return True

        return False
