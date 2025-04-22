from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, column, index):
            if index == len(word):
                return True

            if row < 0 or row >= rows or column < 0 or column >= cols or board[row][column] != word[index]:
                return False

            # Temporarily mark the cell as visited
            temp = board[row][column]
            board[row][column] = '#'

            # Explore all possible directions: up, down, left, right
            found = (dfs(row + 1, column, index + 1) or
                     dfs(row - 1, column, index + 1) or
                     dfs(row, column + 1, index + 1) or
                     dfs(row, column - 1, index + 1))

            # Restore the cell's original value
            board[row][column] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
        
