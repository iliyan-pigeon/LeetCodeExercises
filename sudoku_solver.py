from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            box_row, box_col = (row // 3) * 3, (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[box_row + i][box_col + j] == num:
                        return False

            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in "123456789":
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if backtrack():
                                    return True
                                board[i][j] = "."  # Undo choice
                        return False  # No valid number found
            return True  # Solved successfully

        backtrack()
      
