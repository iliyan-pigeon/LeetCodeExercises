from typing import List


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
      
