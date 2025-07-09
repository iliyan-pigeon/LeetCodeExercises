class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in set(s):
            if i * k in s and i * (k+1) not in s and i * (k+2) not in s:
                return True

        return False
