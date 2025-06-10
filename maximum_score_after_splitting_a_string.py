class Solution:
    def maxScore(self, s: str) -> int:
        result = 0

        for i in range(1, len(s)):
            first, second = s[:i], s[i:]

            if not first or not second:
                continue

            current_one = first.count("0") + second.count("1")

            if current_one > result:
                result = current_one

        return result
