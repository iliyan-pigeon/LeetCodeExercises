class Solution:
    def makeGood(self, s: str) -> str:

        should_run = True

        while should_run:

            for i in range(1, len(s)):
                if s[i] != s[i-1] and s[i].lower() == s[i-1].lower():
                    s = s[:i-1] + s[i+1:]
                    break
            else:
                should_run = False

        return s
