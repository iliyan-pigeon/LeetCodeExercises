from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        they_trust = []
        trusted_ones = []

        for i in range(len(trust)):
            they_trust.append(trust[i][0])
            trusted_ones.append(trust[i][1])

        for i in trusted_ones:
            if i not in they_trust:
                return i

        return -1
      
