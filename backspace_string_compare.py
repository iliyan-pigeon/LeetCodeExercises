class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        while "#" in s:
            i = s.index("#")

            s = s[:i-1]+s[i+1:]

        while "#" in t:
            i = t.index("#")

            t = t[:i-1] + t[i+1:]

        return s == t
