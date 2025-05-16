from typing import List


# Solution 1
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


# Solution 2
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)

        for i in range(len(arr)-1, -1, -1):
            if i + zeroes < len(arr):
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < len(arr):
                    arr[i + zeroes] = 0
