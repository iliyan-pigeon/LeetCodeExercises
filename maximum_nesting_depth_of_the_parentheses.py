class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        for ch in s:
            if ch == "(":
                current_depth += 1
            elif ch == ")":
                current_depth -= 1

            if current_depth > max_depth:
                max_depth = current_depth

        return max_depth
