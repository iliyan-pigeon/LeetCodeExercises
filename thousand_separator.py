class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        else:
            result = ""
            n = str(n)
            counter = 0

            for i in range(len(n)-1, -1, -1):
                result += n[i]
                counter += 1

                if counter == 3:
                    result += "."
                    counter = 0

        return result[::-1]
