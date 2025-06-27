class Solution:
    def countKeyChanges(self, s: str) -> int:
        key_changes = 0
        s = s.lower()

        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                key_changes += 1

        return key_changes
