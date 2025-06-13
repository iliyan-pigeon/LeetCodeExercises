class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        integers = set()
        current = ""

        for ch in word:
            if ch.isnumeric():
                current += ch
            elif ch.isalpha() and current:
                integers.add(current)
                current = ""

        return len(integers)
