from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        
        trust_counts = [0] * (n + 1)
        trusted_by_counts = [0] * (n + 1)
        
        for a, b in trust:
            trust_counts[a] += 1
            trusted_by_counts[b] += 1
        
        for person in range(1, n + 1):
            if trust_counts[person] == 0 and trusted_by_counts[person] == n - 1:
                return person
        
        return -1
        
