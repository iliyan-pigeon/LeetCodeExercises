class Solution(object):
    def isPalindrome(self, s):
        s = "".join([i.lower() for i in s if i.isalnum()])
        s_reversed = "".join([i for i in reversed(s)])

        if s == s_reversed:
            return True
        else:
            return False
          
