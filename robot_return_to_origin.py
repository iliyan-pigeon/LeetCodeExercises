class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {"U": 0, "D": 0, "L": 0, "R": 0}

        for move in moves:
            directions[move] += 1

        if directions["U"] == directions["D"] and directions["L"] == directions["R"]:
            return True

        return False
