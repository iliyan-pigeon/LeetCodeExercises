# Solution 1
from typing import List


class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit


# Solution 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit += price - min_price
                min_price = price

        return profit
