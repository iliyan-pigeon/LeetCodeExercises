class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        amount = 0

        for i in range(len(num)-1, -1, -1):
            if num[i] == "0":
                amount += 1
            else:
                break

        return num[:-amount]
