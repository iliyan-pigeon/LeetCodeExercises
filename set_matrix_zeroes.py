class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        row_set, col_set = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(cols):
                matrix[i][j] = 0

        for j in col_set:
            for i in range(rows):
                matrix[i][j] = 0

        return matrix