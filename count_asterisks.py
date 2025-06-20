class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0

        in_pair = False

        for ch in s:
            if ch == "|" and in_pair is False:
                in_pair = True
            elif ch == "|" and in_pair is True:
                in_pair = False

            if ch == "*" and in_pair is False:
                result += 1

        return result
