from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = [i[0] for i in paths]
        incoming = [i[1] for i in paths]

        for destination in incoming:
            if destination not in outgoing:
                return destination
