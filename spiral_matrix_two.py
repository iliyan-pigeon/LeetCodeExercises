from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        direction = "right"

        for i in range(n):
            matrix.append([0 for j in range(n)])

        should_run = True
        row = 0
        column = 0
        number = 0

        while True:
            number += 1

            matrix[row][column] = number

            if n * n == number:
                break

            if direction == "right":
                if column + 1 == n:
                    direction = "down"
                    row += 1
                elif matrix[row][column+1] != 0:
                    direction = "down"
                    row += 1
                else:
                    column += 1

            elif direction == "down":
                if row + 1 == n:
                    direction = "left"
                    column -= 1
                elif matrix[row+1][column] != 0:
                    direction = "left"
                    column -= 1
                else:
                    row += 1

            elif direction == "left":
                if column - 1 == -1:
                    direction = "up"
                    row -= 1
                elif matrix[row][column-1] != 0:
                    direction = "up"
                    row -= 1
                else:
                    column -= 1

            elif direction == "up":
                if row - 1 == -1:
                    direction = "right"
                    column += 1
                elif matrix[row-1][column] != 0:
                    direction = "right"
                    column += 1
                else:
                    row -= 1

        return matrix
