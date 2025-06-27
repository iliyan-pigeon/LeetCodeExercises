class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) <= 8:
            return len(word)

        result = 0
        add = 1

        for i in range(len(word)):
            if i % 8 == 0 and i != 0:
                add += 1

            result += add

        return result
