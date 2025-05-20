class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet_to_number = {chr(i): i - 64 for i in range(65, 91)}
        result = 0

        for i, ch in enumerate(columnTitle):
            if i == len(columnTitle)-1:
                result += alphabet_to_number[ch]
            else:
                result += alphabet_to_number[ch] * 26

        return result
      
