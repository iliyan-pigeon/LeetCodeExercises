class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        max_vowels = 0

        for i in range(k, len(s)+1):
            current_string = s[i-k:i]
            current_vowels = 0

            for ch in current_string:
                if ch in vowels:
                    current_vowels += 1

            if current_vowels > max_vowels:
                max_vowels = current_vowels
        return max_vowels
