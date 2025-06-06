from typing import List


# Solution 1 (Slow)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = []
        if obstacleGrid[0][0] != 1:
            paths.append([0, 0])
        possible_paths = 0

        end_row = len(obstacleGrid) - 1
        end_column = len(obstacleGrid[0]) - 1

        if end_row == 0 and end_column == 0 and obstacleGrid[end_row][end_column] != 1:
            return 1

        while True:
            paths_to_add = []
            path_added = False

            if not paths:
                break

            for path in paths:
                row, column = path

                if row + 1 <= end_row:
                    if row + 1 == end_row and column == end_column and obstacleGrid[row+1][column] != 1:
                        possible_paths += 1
                        path_added = True
                    elif obstacleGrid[row+1][column] != 1:
                        paths_to_add.append([row+1, column])
                if column + 1 <= end_column:
                    if row == end_row and column + 1 == end_column and not path_added and obstacleGrid[row][column+1] != 1:
                        possible_paths += 1
                    elif obstacleGrid[row][column+1] != 1:
                        paths_to_add.append([row, column+1])

            paths = paths_to_add

        return possible_paths


# Solution 2
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]
        
