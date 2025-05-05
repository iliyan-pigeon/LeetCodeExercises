from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters = set(letters)
        letters = [i for i in letters]
        letters.sort()

        target_index = letters.index(target)

        if target_index == len(letters) - 1:
            return letters[0]

        return letters[target_index+1]
      
