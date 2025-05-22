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
      
