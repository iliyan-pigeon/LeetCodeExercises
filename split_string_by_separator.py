from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            word = word.split(separator)
            result.extend([i for i in word if i != ""])

        return result
