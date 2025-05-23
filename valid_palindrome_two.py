# Solution 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        first_pointer = 0
        second_pointer = len(s)-1

        while first_pointer <= len(s) // 2:
            first_current = s[:first_pointer]+s[first_pointer+1:]
            second_current = s[:second_pointer]+s[second_pointer+1:]

            if first_current == first_current[::-1] or second_current == second_current[::-1]:
                return True

            first_pointer += 1
            second_pointer -= 1

        return False


# Solution 2
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            current = s[:i]+s[i+1:]

            if current == current[::-1]:
                return True

        return False
      
