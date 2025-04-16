from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) ->bool:
        result = False
        checked_some_row = False

        for row in matrix:
            if target == row[-1]:
                result = True
                break
            elif target < row[-1]:
                checked_some_row = True
                for column in row:
                    if column == target:
                        result = True
                        break
            if checked_some_row:
                break

        return result
      
