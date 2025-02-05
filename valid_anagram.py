# Solution 1
class Solution(object):
    def isAnagram(self, s, t):
        result = True

        if len(s) != len(t):
            return False

        for ch in s:
            if s.count(ch) != t.count(ch):
                result = False

        return result

# Solution 2
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


# Solution 3
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
