class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        ones = sorted([i for i, v in enumerate(s) if v == "1"])

        if not ones:
            return False

        if ones == sorted([i for i in range(ones[0], ones[-1]+1)]):
            return True

        return False
