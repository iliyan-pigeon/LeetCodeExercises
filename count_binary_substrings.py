class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        result = 0

        zeros = 0
        ones = 0

        for i, v in enumerate(s):
            if v == "0":
                zeros += 1
            elif v == "1":
                ones += 1

            if ones == zeros and ones != 0:
                result += ones
                if v == "1":
                    zeros = 0
                elif v == "0":
                    ones = 0

        return result
