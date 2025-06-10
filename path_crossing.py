class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}

        row = 0
        col = 0

        for direction in path:
            if direction == "N":
                row -= 1
            elif direction == "S":
                row += 1
            elif direction == "E":
                col -= 1
            elif direction == "W":
                col += 1

            current = (row, col)

            if current in visited:
                return True

            visited.add(current)

        return False
