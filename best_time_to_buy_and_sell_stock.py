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
