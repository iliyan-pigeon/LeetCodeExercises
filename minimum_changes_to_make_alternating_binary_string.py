class Solution:
    def minOperations(self, s: str) -> int:
        result_one = 0
        result_two = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    result_one += 1
                elif s[i] == "0":
                    result_two += 1
            else:
                if s[i] == "1":
                    result_two += 1
                elif s[i] == "0":
                    result_one += 1

        return min(result_one, result_two)
