from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        skip = False

        for i, v in enumerate(arr):

            if skip:
                skip = False
                continue

            if v == 0:
                arr.insert(i, v)
                arr.pop()
                skip = True

        return arr
      
