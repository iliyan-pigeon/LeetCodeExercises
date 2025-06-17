class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        should_skip = 2

        for ch in s:
            if should_skip == 0:
                continue

            if ch == "X":
                result += 1

        return result
