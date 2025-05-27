class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        while "#" in s:
            first = s.index("#")
            second = first + 1

            if first > 0:
                first = first-1
                second -= 1

            s = s[:first]+s[second:]

        while "#" in t:
            first = t.index("#")
            second = first + 1

            if first > 0:
                first = first-1
                second -= 1

            t = t[:first] + t[second:]

        return s == t
