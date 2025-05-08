from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(new_matrix)-1 < j:
                    new_matrix.append([])
                new_matrix[j].append(matrix[i][j])

        return new_matrix
      
