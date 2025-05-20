from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        odd_added = 0
        length = 0

        for ch, amount in count.items():
            if amount % 2 != 0 and odd_added < amount:
                odd_added = amount
            elif amount % 2 == 0:
                length += amount

        return length + odd_added
