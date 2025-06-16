from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        result = all([i == len(words) for i in Counter("".join(words)).values()])

        return result
