class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        result = ""

        for i in range(ones):
            if i == 0:
                result += "0" * (len(s) - ones) + "1"
            else:
                result = "1" + result

        return result
