class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet_to_number = {chr(i): i - 64 for i in range(65, 91)}
        result = 0

        for ch in columnTitle:
            result = result * 26 + alphabet_to_number[ch]

        return result
      
