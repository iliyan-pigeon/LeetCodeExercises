class Solution:
    def secondHighest(self, s: str) -> int:
        numerics = []

        for i in s:
            if i.isnumeric() and i not in numerics:
                numerics.append(i)

        if len(numerics) < 2:
            return -1

        numerics.sort()

        return int(numerics[-2])
