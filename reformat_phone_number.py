class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "")
        number = number.replace(" ", "")
        number = list(number)

        result = []
        current = ""

        for i in range(len(number)):
            if i % 3 == 0 and i != 0:
                result.append(current)
                current = ""

            current += number[i]

        if len(current) == 1:
            current = result[-1][-1] + current
            result[-1] = result[-1][:-1]
            result.append(current)
        else:
            result.append(current)

        return "-".join(result)
