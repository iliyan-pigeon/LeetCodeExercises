from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for number in arr:
            if number not in occurrences:
                occurrences[number] = 0
            occurrences[number] += 1

        if len(set(occurrences.values())) == len(occurrences.values()):
            return True
        return False
