from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        s = Counter(s)

        if len(s) <= k:
            return 0

        return sum(sorted([i for i in s.values()])[:len(s)-k])    
