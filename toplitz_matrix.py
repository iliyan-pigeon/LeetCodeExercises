from typing import List


class Solution:
    def isTeoplitzMatrix(self, matrix: List[List[int]]) -> bool:

        is_valid = True

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])):
                number = matrix[i][j]
                row = i
                col = j
                while row + 1 < len(matrix) and col + 1 < len(matrix[i]):
                    row += 1
                    col += 1

                    if matrix[row][col] != number:
                        is_valid = False
                        break

                if is_valid is False:
                    break

            if is_valid is False:
                break

        return is_valid
      
