from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        differences = 0

        for i, v in enumerate(sorted(heights)):
            if v != heights[i]:
                differences += 1

        return differences
      
