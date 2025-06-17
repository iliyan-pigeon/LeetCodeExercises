from typing import List


# Solution 1
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        substrings_amount = 0

        for pattern in patterns:
            if pattern in word:
                substrings_amount += 1

        return substrings_amount


# Solution 2
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len([pattern for pattern in patterns if pattern in word])
