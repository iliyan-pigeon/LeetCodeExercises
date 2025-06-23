class Solution:
    def partitionString(self, s: str) -> int:
        substrings = 1
        current = ""

        for ch in s:
            if ch in current:
                current = ch
                substrings += 1
            else:
                current += ch

        return substrings
