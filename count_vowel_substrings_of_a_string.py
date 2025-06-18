class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        valid_substrings = []
        vowels = "aeiou"

        for i in range(len(word)):
            right = len(vowels)+i
            current = word[i:right]

            while all([True if i in vowels else False for i in current]) and right <= len(word):
                if all([True if i in current else False for i in vowels]):
                    valid_substrings.append(current)

                right += 1
                current = word[i:right]


        return len(valid_substrings)
