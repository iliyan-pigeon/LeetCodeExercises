class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longest = 0

        zeros = 0
        ones = 0

        for ch in s:
            if ch == "0":
                if ones > 0:
                    ones = 0
                    zeros = 1
                else:
                    zeros += 1
            elif ch == "1":
                if zeros > ones:
                    ones += 1
                else:
                    ones = 0
                    zeros = 0

            if zeros > 0 and ones > 0 and ones*2 > longest:
                longest = ones*2

        return longest
