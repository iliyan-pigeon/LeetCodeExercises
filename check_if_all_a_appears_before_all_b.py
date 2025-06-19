class Solution:
    def checkString(self, s: str) -> bool:
        b_appeared = False

        for ch in s:
            if ch == "b" and not b_appeared:
                b_appeared = True

            if ch == "a" and b_appeared:
                return False

        return True
