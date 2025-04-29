from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island_perimeter = 0

        left_up = -1
        right_down = +1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:

                    if i + left_up >= 0:
                        if grid[i + left_up][j] == 0:
                            island_perimeter += 1
                    else:
                        island_perimeter += 1

                    if i + right_down < len(grid):
                        if grid[i + right_down][j] == 0:
                            island_perimeter += 1
                    else:
                        island_perimeter += 1

                    if j + left_up >= 0:
                        if grid[i][j + left_up] == 0:
                            island_perimeter += 1
                    else:
                        island_perimeter += 1

                    if j + right_down < len(grid[i]):
                        if grid[i][j + right_down] == 0:
                            island_perimeter += 1
                    else:
                        island_perimeter += 1

        return island_perimeter
      
