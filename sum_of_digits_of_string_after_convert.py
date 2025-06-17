class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ""
        for ch in s:
            digits += str(ord(ch)-96)

        for _ in range(k):
            result = 0

            for i in digits:
                result += int(i)

            digits = str(result)

        return result
