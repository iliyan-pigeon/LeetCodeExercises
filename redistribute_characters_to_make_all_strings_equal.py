from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return len("".join(words)) % len(words) == 0
