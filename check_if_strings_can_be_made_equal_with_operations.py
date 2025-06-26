class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False

        if s1 == s2:
            return True

        variations = [f"{s1[2]}{s1[1]}{s1[0]}{s1[3]}", f"{s1[0]}{s1[3]}{s1[2]}{s1[1]}", f"{s1[2]}{s1[3]}{s1[0]}{s1[1]}"]

        if s2 in variations:
            return True

        return False
