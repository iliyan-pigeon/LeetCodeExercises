from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        for word in words:
            current_chars = chars
            valid = True
            for ch in word:
                if ch in current_chars:
                    current_chars = current_chars.replace(ch, "", 1)
                else:
                    valid = False
                    break

            if valid:
                result += len(word)

        return result
