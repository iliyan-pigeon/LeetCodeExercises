class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        should_skip = 0

        for ch in s:
            if should_skip > 0:
                should_skip -= 1
            elif ch == "X":
                result += 1
                should_skip = 2

        return result
