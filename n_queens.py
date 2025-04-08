from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        stack = []
        queens = [-1] * n

        row = 0
        col = 0

        while row < n:
            while col < n:
                if self.is_safe(queens, row, col, n):
                    queens[row] = col
                    stack.append((row, col))
                    row += 1
                    col = 0
                    break
                col += 1

            if col == n or row >= n:

                if row == n:
                    solutions.append(self.format_solution(queens, n))

                if stack:
                    row, col = stack.pop()
                    queens[row] = -1
                    col += 1
                else:
                    break

        return solutions

    def is_safe(self, queens, row, col, n):
        for i in range(row):
            if queens[i] == col or \
                    queens[i] - i == col - row or \
                    queens[i] + i == col + row:
                return False
        return True

    def format_solution(self, queens, n):
        solution = []
        for i in range(n):
            line = ['.'] * n
            line[queens[i]] = 'Q'
            solution.append(''.join(line))
        return solution
    