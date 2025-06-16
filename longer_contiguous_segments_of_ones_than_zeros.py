class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_zeros = 0
        longest_ones = 0

        current_zeros = 0
        current_ones = 0

        for i in range(len(s) + 1):

            if current_zeros > longest_zeros:
                longest_zeros = current_zeros

            if current_ones > longest_ones:
                longest_ones = current_ones

            if i < len(s):
                ch = s[i]
            else:
                break

            if ch == "0":
                current_ones = 0
                current_zeros += 1
            elif ch == "1":
                current_zeros = 0
                current_ones += 1

        return longest_ones > longest_zeros
