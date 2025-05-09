from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]:

                    area += grid[i][j] * 6

                    area -= (grid[i][j] - 1) * 2

                if i > 0:
                    area -= min(grid[i][j], grid[i-1][j]) * 2

                if j > 0:
                    area -= min(grid[i][j], grid[i][j-1]) * 2

        return area
