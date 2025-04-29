from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most_consecutive = 0
        current_consecutive = 0
        
        for i in nums:
            if i == 1:
                current_consecutive += 1
                
                if current_consecutive > most_consecutive:
                    most_consecutive = current_consecutive
            else:
                current_consecutive = 0
                
        return most_consecutive    
