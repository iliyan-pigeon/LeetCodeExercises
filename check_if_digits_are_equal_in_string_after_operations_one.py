class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new = ""

            for i in range(len(s)-1):
                new += str((int(s[i]) + int(s[i+1])) % 10)

            s = new

        return s[0] == s[1]
