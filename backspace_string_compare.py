class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        while "#" in s:
            i = s.index("#")

            if i > 0:
                i = i-1

            s = s[:i]+s[i+1:]

        while "#" in t:
            i = t.index("#")

            if i > 0:
                i = i-1

            t = t[:i] + t[i+1:]

        return s == t
