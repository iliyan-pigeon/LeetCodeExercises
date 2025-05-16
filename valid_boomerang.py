from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        result = True

        rows = []
        cols = []

        for i in range(len(points)):
            rows.append(points[i][0])
            cols.append(points[i][1])

        if len(set(rows)) == 1 or len(set(cols)) == 1 or rows == cols:
            result = False

        return result
      
