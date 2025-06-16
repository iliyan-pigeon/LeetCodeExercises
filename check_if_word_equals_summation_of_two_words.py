class Solution:
    def isSumEqual(self, firstWord: str, secondWord2: str, targetWord: str) -> bool:

        first = int("".join([str(ord(ch)-97) for ch in firstWord]))
        second = int("".join([str(ord(ch)-97) for ch in secondWord2]))
        third = int("".join([str(ord(ch)-97) for ch in targetWord]))

        return first + second == third
