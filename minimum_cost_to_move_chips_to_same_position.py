from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(len([i for i in position if i % 2 == 0]), len([i for i in position if i % 2 != 0]))
