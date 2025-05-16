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

                row_up = row+1
                row_up_cell = [row_up, col]

                row_down = row-1
                row_down_cell = [row_down, col]

                col_right = col+1
                col_right_cell = [row, col_right]

                col_left = col-1
                col_left_cell = [row, col_left]

                if row_up < rows and row_up_cell not in result and row_up_cell not in for_processing:
                    result.append(row_up_cell)
                    for_processing.append(row_up_cell)

                if row_down >= 0 and row_down_cell not in result and row_down_cell not in for_processing:
                    result.append(row_down_cell)
                    for_processing.append(row_down_cell)

                if col_right < cols and col_right_cell not in result and col_right_cell not in for_processing:
                    result.append(col_right_cell)
                    for_processing.append(col_right_cell)

                if col_left >= 0 and col_left_cell not in result and col_left_cell not in for_processing:
                    result.append([row, col-1])
                    for_processing.append([row, col-1])

            for_processing = for_processing[processed:]

        return result
