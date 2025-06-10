class Solution:
    def maxScore(self, s: str) -> int:
        result = 0

        for i in range(1, len(s)):
            first, second = s[:i], s[i:]
            current_one = first.count("0") + second.count("1")
            current_two = first.count("1") + second.count("0")

            if current_one > result:
                result = current_one

            if current_two > result:
                result = current_two

        return result
