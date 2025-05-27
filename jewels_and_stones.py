# Solution 1
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        for i in stones:
            if i in jewels:
                result += 1

        return result


# Solution 2
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([i for i in stones if i in jewels])
