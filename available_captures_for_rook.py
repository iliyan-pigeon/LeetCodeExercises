from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[int]]) -> int:
        result = 0
        r_row = None
        r_column = None

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    r_row = i
                    r_column = j
                    break
            if r_row is not None:
                break

        up = r_row
        down = r_row
        left = r_column
        right = r_column

        directions = []

        while True:

            if up + 1 < len(board) and "up" not in directions:
                up += 1
                if board[up][r_column] == "p":
                    result += 1
                    directions.append("up")
                elif board[up][r_column] == "B":
                    directions.append("up")
            elif up + 1 == len(board):
                up += 1
                directions.append("up")

            if down - 1 >= 0 and "down" not in directions:
                down -= 1
                if board[down][r_column] == "p":
                    result += 1
                    directions.append("down")
                elif board[down][r_column] == "B":
                    directions.append("down")
            elif down - 1 == -1:
                down -= 1
                directions.append("down")

            if right + 1 < len(board[0]) and "right" not in directions:
                right += 1
                if board[r_row][right] == "p":
                    result += 1
                    directions.append("right")
                elif board[r_row][right] == "B":
                    directions.append("right")
            elif right + 1 == len(board[0]):
                right += 1
                directions.append("right")

            if left - 1 >= 0 and "left" not in directions:
                left -= 1
                if board[r_row][left] == "p":
                    result += 1
                    directions.append("left")
                elif board[r_row][left] == "B":
                    directions.append("left")
            elif left - 1 == -1:
                left -= 1
                directions.append("left")

            if all([i in directions for i in ["up", "down", "left", "right"]]):
                break

        return result

