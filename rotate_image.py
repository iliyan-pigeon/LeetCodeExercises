class Solution(object):
    def rotate(self, matrix):
        transposed_matrix = list(zip(*matrix))

        rotated_matrix = [list(row)[::-1] for row in transposed_matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = rotated_matrix[i][j]

        return rotated_matrix
