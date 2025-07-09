class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)-k+1):
            current = s[i:i + k]

            if len(set(current)) == 1:
                if i == 0 and i + k == len(s):
                    return True
                elif i == 0:
                    if s[i+k] != current[0]:
                        return True
                elif i+k == len(s):
                    if s[i-1] != current[0]:
                        return True
                elif s[i-1] != current[0] and s[i+k] != current[0]:
                    return True

        return False
