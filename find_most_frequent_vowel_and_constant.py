from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        s = Counter(s)

        vowel_fr = 0
        const_fr = 0

        for ch, fr in s.items():
            if ch in "aeiou" and fr > vowel_fr:
                vowel_fr = fr
            elif ch not in "aeiou" and fr > const_fr:
                const_fr = fr

        return vowel_fr + const_fr
