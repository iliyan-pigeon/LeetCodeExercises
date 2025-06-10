class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            result = "a" * n
        else:
            result = "a" * (n - 1) + "b"

        return result
