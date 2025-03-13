from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        columns = {}

        pairs_amount = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if row not in rows:
                    rows[row] = []
                rows[row].append(str(grid[row][column]))

                if column not in columns:
                    columns[column] = []
                columns[column].append(str(grid[row][column]))

        columns_values = [value for value in columns.values()]

        for value in rows.values():
            if value in columns_values:
                pairs_amount += columns_values.count(value)

        return pairs_amount


a = Solution()
print(a.equalPairs([[11,1],[1,11]]))

