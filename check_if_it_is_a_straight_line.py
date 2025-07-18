from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        coordinates.sort()
        previous = coordinates[0]
        first_distance = 0
        second_distance = 0

        first = set([i[0] for i in coordinates])
        second = set([i[1] for i in coordinates])

        if len(first) == 1 or len(second) == 1:
            return True

        for i in range(1, len(coordinates)):
            if i == 1:
                first_distance = coordinates[i][0] - previous[0]
                second_distance = coordinates[i][1] - previous[1]
            if coordinates[i][0] - previous[0] > first_distance or \
                    coordinates[i][1] - previous[1] > second_distance:
                return False
            previous = coordinates[i]

        return True
