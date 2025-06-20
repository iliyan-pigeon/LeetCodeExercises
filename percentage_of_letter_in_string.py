class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        elif letter == set(s):
            return 100

        return int((s.count(letter) / len(s)) * 100)
