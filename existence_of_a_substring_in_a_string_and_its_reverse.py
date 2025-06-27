class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        for i in range(2, len(s)+1):
            current = s[i-2:i][::-1]
            if s[i-2:i][::-1] in s:
                return True

        return False
