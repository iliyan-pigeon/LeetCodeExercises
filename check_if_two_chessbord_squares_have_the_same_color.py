class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1, row1 = list(coordinate1)
        col2, row2 = list(coordinate2)

        if ord(col1) % 2 != 0:
            if int(row1) % 2 != 0:
                first_color = "black"
            else:
                first_color = "white"
        else:
            if int(row1) % 2 != 0:
                first_color = "white"
            else:
                first_color = "black"

        if ord(col2) % 2 != 0:
            if int(row2) % 2 != 0:
                second_color = "black"
            else:
                second_color = "white"
        else:
            if int(row2) % 2 != 0:
                second_color = "white"
            else:
                second_color = "black"

        return first_color == second_color
