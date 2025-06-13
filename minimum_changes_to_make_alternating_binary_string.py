class Solution:
    def minOperations(self, s: str) -> int:
        result = 0
        s = list(s)

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                result += 1

                if s[i+1] == "0":
                    s[i+1] = "1"
                else:
                    s[i+1] = "0"

        return result
