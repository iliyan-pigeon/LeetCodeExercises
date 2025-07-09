from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counter_s = Counter(s)

        for i in range(len(s)-1):
            if int(s[i]) != int(s[i+1]) and int(s[i]) == counter_s[s[i]] and int(s[i+1]) == counter_s[s[i+1]]:
                return s[i:i+2]

        return ""
