class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.index(ch)

        word = word[:index+1][::-1] + word[index+1:]

        return word
