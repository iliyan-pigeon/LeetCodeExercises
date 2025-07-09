class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        missing_index = p.index("*")

        first = p[:missing_index]
        second = p[missing_index+1:]

        start = 0
        end = len(s)

        if first in s:
            start = s.index(first) + len(first)

        if second in s:
            end = s[start:].index(second) + start

        result = f"{first}{s[start:end]}{second}"

        if len(result) == len(s):
            return False

        return result in s
