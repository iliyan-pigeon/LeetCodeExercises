class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            current = s[:i]+s[i+1:]

            if current == current[::-1]:
                return True

        return False
      
