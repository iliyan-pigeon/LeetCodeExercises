from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return sorted([len(i.split(" ")) for i in sentences])[-1]
