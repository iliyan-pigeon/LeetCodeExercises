class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_number = False

        while not odd_number:
            if num == "":
                return ""
            
            if int(num) % 2 != 0:
                odd_number = num

            num = num[:-1]

        return odd_number
