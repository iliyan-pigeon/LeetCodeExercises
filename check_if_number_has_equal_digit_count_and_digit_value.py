from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        nums_count = Counter(num)

        for i in range(len(num)):
            if str(i) not in nums_count and int(num[i]) != 0:
                return False
            elif nums_count[str(i)] != int(num[i]):
                return False

        return True
