from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        moves = Counter(moves)

        if moves["L"] >= moves["R"]:
            return moves["L"] + moves["_"] - moves["R"]

        return moves["R"] + moves["_"] - moves["L"]
