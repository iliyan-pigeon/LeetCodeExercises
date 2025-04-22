from typing import List


# Solution 1
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, column, index):
            if index == len(word):
                return True

            if row < 0 or row >= rows or column < 0 or column >= cols or board[row][column] != word[index]:
                return False

            # Temporarily mark the cell as visited
            temp = board[row][column]
            board[row][column] = '#'

            # Explore all possible directions: up, down, left, right
            found = (dfs(row + 1, column, index + 1) or
                     dfs(row - 1, column, index + 1) or
                     dfs(row, column + 1, index + 1) or
                     dfs(row, column - 1, index + 1))

            # Restore the cell's original value
            board[row][column] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# Solution 2
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        word_length = len(word)

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for column in range(cols):
                stack = [(row, column, 0)]
                visited = set()

                while stack:
                    current_r, current_c, index = stack.pop()

                    if index == word_length:
                        return True

                    if not is_valid(current_r, current_c) or (current_r, current_c) in visited or board[current_r][
                        current_c] != word[index]:
                        continue

                    visited.add((current_r, current_c))

                    for dr, dc in directions:
                        stack.append((current_r + dr, current_c + dc, index + 1))

                    # Remove the current cell from visited to allow other paths to use it
                    visited.remove((current_r, current_c))

        return False
