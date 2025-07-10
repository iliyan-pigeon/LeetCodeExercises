class Solution:
    def myAtoi(self, s: str) -> int:
        sign = "+"
        digit_appeared = False
        digit = ""

        for ch in s:
            if digit_appeared and not ch.isnumeric():
                break
            if not digit_appeared and ch.isnumeric():
                digit_appeared = True

            if ch == "-":
                sign = "-"
            elif ch == "0":
                continue
            else:
                digit += ch

        if sign == "-":
            return -int(digit)

        return int(digit)
