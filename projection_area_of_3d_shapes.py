from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        result = 0

        columns = {}

        for i in range(len(grid)):
            result += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    result += 1

                if j not in columns:
                    columns[j] = 0

                if columns[j] < grid[i][j]:
                    columns[j] = grid[i][j]

        for v in columns.values():
            result += v

        return result
      
