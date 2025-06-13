class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        diff_indexes = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indexes.append(i)

        if len(diff_indexes) != 2:
            return False

        if s1[diff_indexes[0]] == s2[diff_indexes[1]] and s1[diff_indexes[1]] == s2[diff_indexes[0]]:
            return True

        return False
