from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)

        for domino in dominoes:
            normalized = tuple(sorted(domino))
            count[normalized] += 1

        num_pairs = 0
        for key, value in count.items():
            if value > 1:
                num_pairs += value * (value - 1) // 2

        return num_pairs
