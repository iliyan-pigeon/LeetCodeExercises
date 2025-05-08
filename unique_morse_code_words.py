from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                      "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                      "y": "-.--", "z": "--.."}

        combinations = set()

        for word in words:
            current_combination = ""

            for ch in word:
                current_combination += morse_code[ch]

            combinations.add(current_combination)

        return len(combinations)
      
