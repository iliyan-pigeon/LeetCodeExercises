from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        recommended_amount = int(len(candyType) / 2)
        unique_candies = len(set(candyType))

        return min(recommended_amount, unique_candies)
      
