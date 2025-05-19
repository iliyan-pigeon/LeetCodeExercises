from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        result = min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))

        return result
      
