# Solution 1
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        missing_index = p.index("*")

        first = p[:missing_index]
        second = p[missing_index+1:]

        start = 0
        end = len(s)

        if first in s:
            start = s.index(first) + len(first)

        if second in s[start:]:
            end = s[start:].index(second) + start

        result = f"{first}{s[start:end]}{second}"

        return result in s


# Solution 2
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        i = 0
        for t in p.split("*"):
            j = s.find(t, i)

            if j == -1:
                return False

            i = j + len(t)

        return True
