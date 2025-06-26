from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = "".join([i[0] for i in words])

        return acronym == s
