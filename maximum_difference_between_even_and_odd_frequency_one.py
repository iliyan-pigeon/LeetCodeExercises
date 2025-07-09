from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_odd = len(s)

        max_even = 0
        min_even = len(s)

        s = Counter(s)

        for v in s.values():

            if v % 2 == 0:
                if max_even < v:
                    max_even = v
                elif min_even > v:
                    min_even = v
            else:
                if max_odd < v:
                    max_odd = v
                elif min_odd > v:
                    min_odd = v

        return max(abs(max_odd - min_even), abs(max_even - min_odd))
