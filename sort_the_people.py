class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        the_dict = {names[i]: heights[i] for i in range(len(names))}

        result = [k for k, v in sorted(the_dict.items(), key=lambda item: item[1], reverse=True)]

        return result
