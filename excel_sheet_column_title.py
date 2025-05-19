class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            print(columnNumber / 26)
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))
            columnNumber //= 26

        return ''.join(result[::-1])
      
