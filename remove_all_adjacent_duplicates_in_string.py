class Solution:
    def removeDuplicates(self, s: str) -> str:
        finished = False
        while not finished:
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[:i]+s[i+2:]
                    break
            else:
                finished = True

        return s
