from typing import List


# Solution 1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        known = []
        unknown = []

        for element in arr1:
            if element not in arr2:
                unknown.append(element)
            else:
                known.append(element)

        order = {item: index for index, item in enumerate(arr2)}

        known.sort(key=lambda x: order[x])
        known.extend(sorted(unknown))

        return known


# Solution 2
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for arr in arr1:
            if arr in d:
                d[arr] += 1
            else:
                d[arr] = 1
        res1 = []
        res2 = []
        for key in arr2:
            if key in d.keys():
                res1.extend([key] * d[key])
        for key in d.keys():
            if key not in arr2:
                res2.extend([key] * d[key])
        if len(res2) > 0:
            res2.sort()
            arr1 = res1 + res2
        elif len(res2) == 0:
            arr1 = res1
        return arr1
