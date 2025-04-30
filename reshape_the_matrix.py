from typing import List


# Solution 1
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        nums = []

        for i in range(rows):
            for j in range(cols):
                nums.append(mat[i][j])

        new_mat = []

        for i in range(r):
            current_row = []
            for j in range(c):
                current_row.append(nums.pop(0))

            new_mat.append(current_row)

        return new_mat


# Solution 2
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]


# Solution 3
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [num for row in mat for num in row]
        new_mat = []

        for i in range(r):
            new_mat.append(flat[i * c:(i + 1) * c])

        return new_mat
  
