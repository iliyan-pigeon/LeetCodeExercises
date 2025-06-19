from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        s = s.split(":")

        col_start, row_start = list(s[0])
        col_end, row_end = list(s[1])
        current_row = row_start

        while ord(col_start) <= ord(col_end):
            while int(current_row) <= int(row_end):
                result.append(f"{col_start}{current_row}")
                current_row = int(current_row) + 1

            col_start = chr(ord(col_start)+1)
            current_row = row_start

        return result
