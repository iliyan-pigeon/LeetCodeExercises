class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = 0

        for i, v in enumerate(number):
            if v == digit:
                current = number[:i]+number[i+1:]

                if int(current) > result:
                    result = int(current)

        return str(result)
