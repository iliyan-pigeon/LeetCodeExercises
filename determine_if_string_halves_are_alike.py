class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        splitter = len(s) // 2

        left, right = s[:splitter], s[splitter:]

        vowels = "aeiouAEIOU"

        left_count = len([i for i in left if i in vowels])
        right_count = len([i for i in right if i in vowels])

        return left_count == right_count
