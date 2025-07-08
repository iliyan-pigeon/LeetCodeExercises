class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_odd = 0
        sum_even = 0

        for i in range(len(num)):
            if i % 2 != 0:
                sum_odd += int(num[i])
            else:
                sum_even += int(num[i])

        return sum_odd == sum_even
