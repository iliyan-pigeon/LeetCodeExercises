class Solution:
    def myAtoi(self, s: str) -> int:
        sign = "+"
        digit_appeared = False
        digit = ""

        for ch in s:
            if digit_appeared and ch == "-":
                break
            elif ch == "-":
                sign = "-"
            elif not ch.isnumeric():
                break
            elif not digit_appeared and ch.isnumeric():
                digit_appeared = True

            digit += ch

        if digit == "":
            return 0

        if sign == "-":
            return -int(digit)

        return int(digit)
