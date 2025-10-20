from collections import Counter
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        positions = Counter(position)
        result = 0
        position_to_go = None

        for k, v in sorted(positions.items(), key=lambda item: item[1], reverse=True):
            pass


a = Solution()
print(a.minCostToMoveChips([2, 2, 3]))
