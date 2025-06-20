class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        start = 0
        end = k

        result = 0

        while end <= len(str(num)):
            substring = str(num)[start:end]

            if int(substring) > 0 and num % int(substring) == 0:
                result += 1

            start += 1
            end += 1

        return result
