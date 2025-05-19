from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start < destination:
            result = min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))
        else:
            result = min(sum(distance[destination:start]), sum(distance[start:]) + sum(distance[:destination]))

        return result
        
