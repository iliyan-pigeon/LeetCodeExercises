class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)-1):
            if len({int(s[i]) % 2 == 0, int(s[i+1]) % 2 == 0}) == 1 and int(s[i]) > int(s[i+1]):
                s[i], s[i+1] = s[i+1], s[i]
                break

        return "".join(s)
