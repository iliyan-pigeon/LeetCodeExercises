from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result = [[rCenter, cCenter]]
        for_processing = [[rCenter, cCenter]]

        while len(result) < rows * cols:
            processed = len(for_processing)

            for cell in for_processing:
                row = cell[0]
                col = cell[1]

                if row+1 < rows and [row+1, col] not in result and [row+1, col] not in for_processing:
                    result.append([row+1, col])
                    for_processing.append([row+1, col])

                if row-1 >= 0 and [row-1, col] not in result and [row-1, col] not in for_processing:
                    result.append([row-1, col])
                    for_processing.append([row-1, col])

                if col+1 < cols and [row, col+1] not in result and [row, col+1] not in for_processing:
                    result.append([row, col+1])
                    for_processing.append([row, col+1])

                if col-1 >= 0 and [row, col-1] not in result and [row, col-1] not in for_processing:
                    result.append([row, col-1])
                    for_processing.append([row, col-1])

            for_processing = for_processing[processed:]

        return result
      
