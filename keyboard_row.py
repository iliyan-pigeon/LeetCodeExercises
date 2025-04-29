from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_line = "qwertyuiop"
        second_line = "asdfghjkl"
        third_line = "zxcvbnm"

        result = []

        for word in words:
            line = None
            valid_word = True
            for ch in word:
                if line is None:
                    if ch.lower() in first_line:
                        line = first_line
                    elif ch.lower() in second_line:
                        line = second_line
                    elif ch.lower() in third_line:
                        line = third_line
                elif ch.lower() not in line:
                    valid_word = False
                    break

            if valid_word:
                result.append(word)

        return result
