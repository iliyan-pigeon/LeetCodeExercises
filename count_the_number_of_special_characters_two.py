class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_chars = 0

        for ch in set(word):
            if ch.islower() and ch.upper() in word and ch not in word[word.index(ch.upper()):]:
                special_chars += 1

        return special_chars
