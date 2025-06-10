class Solution:
    def maxPower(self, s: str) -> int:
        first = 0
        second = 1

        result = 0

        while second <= len(s):
            current = s[first:second]

            if len(set(current)) == 1:
                if len(current) > result:
                    result = len(current)
                second += 1

            else:
                first += 1

        return result
