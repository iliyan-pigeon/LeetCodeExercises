class Solution(object):
    def isPalindrome(self, s):
        s = "".join([i.lower() for i in s if i.isalnum()])
        s_reversed = "".join([i for i in reversed(s)])

        if s == s_reversed:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s)-1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
