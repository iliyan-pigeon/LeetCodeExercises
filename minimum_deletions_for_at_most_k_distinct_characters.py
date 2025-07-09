class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        s = Counter(s)

        distinct = len([i for i in s.values() if i == 1])

        if distinct <= 2:
            return 0

        return distinct - 2
