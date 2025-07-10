class Solution:
    def myAtoi(self, s: str) -> int:
        sign = "+"
        digit_appeared = False
        digit = ""

        for ch in s.strip():
            if digit_appeared and ch == "-":
                break
            elif ch == "-":
                sign = "-"
                continue
            elif not ch.isnumeric():
                break
            elif not digit_appeared and ch.isnumeric():
                digit_appeared = True

            digit += ch

        if digit == "":
            return 0

        if sign == "-":
            if -int(digit) < -(2**31):
                return -(2**31)

            return -int(digit)

        if int(digit) > 2**31-1:
                return 2**31-1
        return int(digit)