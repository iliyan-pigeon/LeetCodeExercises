# Solution 1
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        return chr(sum([ord(i) for i in t]) - sum([ord(i) for i in s]))


# Solution 2
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        return [i for i in t if i not in s][0]
