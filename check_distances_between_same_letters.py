from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        s_distances = {}

        valid = True

        for i, ch in enumerate(s):
            if ch not in s_distances:
                s_distances[ch] = []
            s_distances[ch].append(i)

            if len(s_distances[ch]) == 2:
                b = abs(s_distances[ch][0] - s_distances[ch][1]) - 1
                c = distance[ord(ch)-97]
                if b != c:
                    valid = False
                    break

        return valid
