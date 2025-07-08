from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = []
        current_number = 0

        for i in range(n):
            current_row = []
            for j in range(n):
                current_row.append(current_number)
                current_number += 1
            matrix.append(current_row)

        row, col = 0, 0

        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "RIGHT":
                col += 1
            elif command == "LEFT":
                col -= 1

        return matrix[row][col]
