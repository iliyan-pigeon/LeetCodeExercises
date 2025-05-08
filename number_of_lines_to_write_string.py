from typing import List


class Solution:
    def numberOfLines(self, width: List[int], s: str) -> List[int]:
        index_mapping = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10,
                         "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20,
                         "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

        row_pixels = 0
        rows_count = 1

        for ch in s:
            current_pixels = width[index_mapping[ch]]

            if row_pixels + current_pixels > 100:
                rows_count += 1
                row_pixels = current_pixels

            else:
                row_pixels += current_pixels

        return [rows_count, row_pixels]
      
