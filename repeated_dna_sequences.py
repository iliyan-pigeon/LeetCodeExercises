from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        substrings = {}
        left = 0
        right = 10

        while right <= len(s):
            current = s[left:right]
            if current not in substrings:
                substrings[current] = 0
            substrings[current] += 1

            left += 1
            right += 1

        return [k for k, v in substrings.items() if v > 1]
