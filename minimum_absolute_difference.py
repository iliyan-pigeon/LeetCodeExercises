from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif = float('inf')
        pairs = []

        for i in range(1, len(arr)):
            current_dif = arr[i] - arr[i-1]
            if current_dif < min_dif:
                min_dif = current_dif
                pairs = [[arr[i-1], arr[i]]]
            elif current_dif == min_dif:
                pairs.append([arr[i-1], arr[i]])

        return pairs
      
