class Solution:
    def canBeTypeWords(self, text: str, brokenLetters: str) -> int:

        result = 0

        for word in text.split(" "):
            valid = True

            for ch in word:
                if ch in brokenLetters:
                    valid = False
                    break

            if valid:
                result += 1
                
        return result
