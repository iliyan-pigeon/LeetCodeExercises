class Solution(object):
    def romanToInt(self, s):
        numbers_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        last_character = 1

        for ch in reversed(s):
            if numbers_dict[ch] < last_character:
                result -= numbers_dict[ch]
            else:
                result += numbers_dict[ch]

            last_character = numbers_dict[ch]

        return result
