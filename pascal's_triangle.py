from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            current_row = []

            if i == 0:
                current_row.append(1)
                result.append(current_row)
                continue

            for j in range(i+1):
                previous_row = result[-1]
                if j == 0:
                    current_row.append(previous_row[j])
                elif j == i:
                    current_row.append(previous_row[j-1])
                else:
                    current_row.append(previous_row[j] + previous_row[j-1])

            result.append(current_row)

        return result
        
