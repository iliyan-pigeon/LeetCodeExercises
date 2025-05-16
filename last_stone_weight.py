from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) >= 2:
            stones.sort()
            biggest = stones.pop()
            second_biggest = stones.pop()

            if biggest != second_biggest:
                stones.append(biggest - second_biggest)

        if len(stones) == 0:
            return 0

        return stones[0]
      
