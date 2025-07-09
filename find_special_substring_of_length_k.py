class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)):
            current = s[i:i + k]

            if len(set(current)) == 1:
                if i == 0 and s[i + k] != current[0] or \
                        s[i] != current[0] and i + k == len(s) or \
                        s[i] != current[0] and s[i + k] != current[0]:
                    return True

        return False
