from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = Counter([i for i in text if i in "balloon"])
        result = 0
        valid = True

        while valid:

            for ch in "balloon":
                if ch not in text:
                    valid = False
                    break
                elif text[ch] == 0:
                    valid = False
                    break
                else:
                    text[ch] -= 1

            if valid:
                result += 1

        return result
