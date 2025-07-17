from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        coordinates.sort()
        previous = coordinates[0]

        for i in range(1, len(coordinates)):
            if coordinates[i][0] - previous[0] > 1 or \
                    coordinates[i][1] - previous[1] > 1:
                return False
            previous = coordinates[i]

        return True
