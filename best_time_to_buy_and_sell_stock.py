# Solution 1
class Solution(object):
    def maxProfit(self, prices):
    
        min_price = float('inf') 
        max_profit = 0            

    
        for price in prices:
        
            if price < min_price:
                min_price = price
            else:

                profit = price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit


# Solution 2
import sys


class Solution(object):
    def maxProfit(self, prices):
        biggest_distance = - sys.maxsize
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                current_distance = prices[j] - prices[i]

                if biggest_distance < current_distance:
                    biggest_distance = current_distance

        return biggest_distance
