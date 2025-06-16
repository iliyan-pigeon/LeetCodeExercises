class Solution:
    def largest_odd_number_in_string(self, num: str) -> str:
        odd_number = False

        while not odd_number:
            if int(num) % 2 != 0:
                odd_number = num

            num = num[:-1]

            if num == "":
                return ""

        return odd_number
