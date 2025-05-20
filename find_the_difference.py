# Solution 1
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        return chr(sum([ord(i) for i in t]) - sum([ord(i) for i in s]))


# Solution 2
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        count = Counter(t)

        for i, v in count.items():
            for j in range(v):
                if i not in s:
                    return i
                s = s.replace(i, "", 1)
