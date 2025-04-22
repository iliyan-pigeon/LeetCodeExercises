from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = []
        result = None

        for i in range(rowIndex+1):
            current_row = []

            if i == 0:
                current_row.append(1)
                result = current_row
                i = -1

            for j in range(i+1):
                previous_row = rows[-1]
                if j == 0:
                    current_row.append(previous_row[j])
                elif j == i:
                    current_row.append(previous_row[j-1])
                else:
                    current_row.append(previous_row[j] + previous_row[j-1])

            rows.append(current_row)

            if i == rowIndex:
                result = current_row
                break

        return result
