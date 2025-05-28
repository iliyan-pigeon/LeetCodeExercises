from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = [i for i in s1 if i not in s2]
        result.extend([i for i in s2 if i not in s1])

        return result
