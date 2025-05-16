from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points

        if p1 == p2 or p1 == p3 or p2 == p3:
            return False

        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        return (x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) != 0
