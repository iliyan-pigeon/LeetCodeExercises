from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if [i[0] for i in coordinates] == [i for i in range(coordinates[0][0], coordinates[-1][0]+1)] and \
                [i[1] for i in coordinates] == [i for i in range(coordinates[0][1], coordinates[-1][1]+1)]:
            return True
        return False
