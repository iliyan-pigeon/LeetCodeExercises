import sys
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        smallest_index = sys.maxsize

        combined = set(list1).union(set(list2))

        for word in combined:
            if word in list1 and word in list2:
                current_index = list1.index(word) + list2.index(word)

                if smallest_index > current_index:
                    smallest_index = current_index
                    result = [word]
                elif smallest_index == current_index:
                    result.append(word)

        return result
      
