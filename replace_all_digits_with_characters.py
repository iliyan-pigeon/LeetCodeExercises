class Solution:
    def replaceDigits(self, s: str) -> str:
        for i, ch in enumerate(s):
            if ch.isnumeric():
                s = s.replace(ch, chr(ord(s[i-1])+int(ch)), 1)

        return s
