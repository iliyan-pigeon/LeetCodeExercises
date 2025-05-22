# Solution 1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_copy = s
        counter = 0

        while counter <= len(s)//2:
            s_copy = s_copy[-1]+s_copy[:-1]
            counter += 1

            if s_copy == s:
                return True

        return False


# Solution 2
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        if not str:
            return False

        ss = (s+s)[1:-1]
        return ss.find(s) != -1
