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
