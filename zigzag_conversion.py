class Solution(object):
    def convert(self, s, numRows):
        matrix = []
        counter_row = 0
        action = "plus"

        for i in range(numRows):
            matrix.append([])

        for i in s:

            if counter_row == 0:
                action = "plus"
            elif counter_row == numRows - 1:
                action = "minus"

            matrix[counter_row].append(i)

            if action == "plus" and counter_row + 1 < numRows:
                counter_row += 1
            elif action == "minus":
                counter_row -= 1

        result = ""

        for the_row in matrix:
            for ch in the_row:
                result += ch

        return result
