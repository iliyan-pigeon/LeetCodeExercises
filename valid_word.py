class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        vowel = False
        constant = False

        for ch in word:
            if ch in "aeiou" and ch.isalpha():
                vowel = True

            elif ch not in "aeiou" and ch.isalpha():
                constant = True

            if constant and vowel:
                break

        return vowel is True and constant is True
