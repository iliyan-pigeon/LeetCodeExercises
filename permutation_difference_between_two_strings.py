class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indexes = {}

        for i in range(len(s)):
            if s[i] not in indexes:
                indexes[s[i]] = []

            if t[i] not in indexes:
                indexes[t[i]] = []

            indexes[s[i]].append(i)
            indexes[t[i]].append(i)

        return sum([abs(v[0] - v[1]) for v in indexes.values()])
