class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n

        seq = [0, 1]
        while n > seq[-1]:
            for i in range(n):
                seq.append(seq[-1] + seq[-2])
        return seq[-2] + seq[-3]
