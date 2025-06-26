# Solution 1
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        amount = 0

        for i in range(len(num)-1, -1, -1):
            if num[i] == "0":
                amount += 1
            else:
                break

        if amount > 0:
            return num[:-amount]

        return num


# Solution 2
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(num).rstrip('0')
