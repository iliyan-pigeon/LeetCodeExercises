from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0

        min_even = len(s)

        s = Counter(s)

        for v in s.values():

            if v % 2 == 0:
                if min_even > v:
                    min_even = v
            else:
                if max_odd < v:
                    max_odd = v

        return max_odd - min_even