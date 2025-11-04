class Solution:
    def reverse(self, x: int) -> int:

        result = None

        if str(x)[0].isdigit():
            result = int(str(x)[::-1])
        else:
            result = int(f"{str(x)[0]}{str(x)[:0:-1]}")

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result          