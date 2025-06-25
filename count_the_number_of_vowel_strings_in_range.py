from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel_strings = 0
        vowels = "aeiou"

        for i in range(left, right+1):
            word = words[i]

            if word[0] in vowels and word[-1] in vowels:
                vowel_strings += 1

        return vowel_strings
