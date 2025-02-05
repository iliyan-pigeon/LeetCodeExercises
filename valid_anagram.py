class Solution(object):
    def isAnagram(self, s, t):
        result = True

        if len(s) != len(t):
            return False

        for ch in s:
            if s.count(ch) != t.count(ch):
                result = False

        return result
