class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        for i in range(len(s)-1):
            if s[i] == "1" and s[i+1] == "1":
                return True

        return False
