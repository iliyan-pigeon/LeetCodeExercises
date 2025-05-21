from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False

        for amount in count.values():
            if amount % 2 == 0:
                length += amount
            else:
                length += amount - 1
                odd_found = True

        if odd_found:
            length += 1

        return length
        
