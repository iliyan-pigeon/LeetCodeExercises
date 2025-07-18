# Solution 1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


# Solution 2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x
        for i in range(n-1):
            result *= x

        return result
