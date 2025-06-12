# Solution 1
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        result = 0

        for j in range(len(sequence)):

            consecutive = 0

            for i in range(j, len(sequence), len(word)):
                if sequence[i:i+len(word)] == word:
                    consecutive += 1

                    if consecutive > result:
                        result = consecutive

                else:
                    consecutive = 0

        return result


# Solution 2
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0] * (n + 1)
        max_repeat = 0

        for i in range(m, n + 1):
            if sequence[i - m:i] == word:
                dp[i] = dp[i - m] + 1
                max_repeat = max(max_repeat, dp[i])

        return max_repeat
