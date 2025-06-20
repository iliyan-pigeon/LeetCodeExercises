from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        frequency_target = Counter(target)
        frequency_s = Counter(s)

        result = len(s)

        for ch, fr in frequency_target.items():
            if ch not in frequency_s:
                return 0
            elif frequency_s[ch] < fr:
                return 0
            elif result > frequency_s[ch] // fr:
                result = frequency_s[ch] // fr

        return result
