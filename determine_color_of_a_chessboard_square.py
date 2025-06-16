class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col, row = list(coordinates)

        if col == "a":
            if int(row) % 2 != 0:
                return False
            return True
        elif col == "b":
            if int(row) % 2 != 0:
                return True
            return False
        elif col == "c":
            if int(row) % 2 != 0:
                return False
            return True
        elif col == "d":
            if int(row) % 2 != 0:
                return True
            return False
        elif col == "e":
            if int(row) % 2 != 0:
                return False
            return True
        elif col == "f":
            if int(row) % 2 != 0:
                return True
            return False
        elif col == "g":
            if int(row) % 2 != 0:
                return False
            return True
        elif col == "h":
            if int(row) % 2 != 0:
                return True
            return False
