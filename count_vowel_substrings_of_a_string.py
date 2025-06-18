class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        valid_substrings = []
        vowels = "aeiou"

        for i in range(len(word)-len(vowels)):
            right = len(vowels)+i
            current = word[i:right]

            while all([True if i in vowels else False for i in current]):
                if current not in valid_substrings and all([True if i in current else False for i in vowels]):
                    valid_substrings.append(current)

                right += 1
                current = word[i:right]


        return valid_substrings
