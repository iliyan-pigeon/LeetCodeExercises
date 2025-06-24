from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        the_dict = {heights[i]: names[i] for i in range(len(names))}

        result = [v for k, v in sorted(the_dict.items(), key=lambda item: item[0], reverse=True)]

        return result
