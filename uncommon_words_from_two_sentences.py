from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split()
        combined = s1 + s2

        return [i for i in combined if i not in s1 or i not in s2]
