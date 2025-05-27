from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        result = []

        start = 0
        end = 0
        current = None

        for i, v in enumerate(s):

            if v != current:
                if end-start+1 >= 3:
                    result.append([start, end])
                start = i
                end = i
                current = v

            elif v == current:
                end = i
                if i == len(s)-1 and end-start+1 >= 3:
                    result.append([start, end])

        return result
