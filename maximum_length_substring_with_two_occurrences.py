from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 1

        result = 0

        while left < len(s):
            current = s[left:right]

            if max([v for v in Counter(current).values()]) <= 2:
                right += 1
                if len(current) > result:
                    result = len(current)
            else:
                left += 1

            if right >= len(s)+1:
                left += 1

        return result
