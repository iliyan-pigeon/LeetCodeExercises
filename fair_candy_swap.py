from typing import List


# Solution 1
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        for i in aliceSizes:
            for j in bobSizes:
                if alice_total - i + j == bob_total + i - j:
                    return [i, j]


# Solution 2
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        delta = (alice_total - bob_total) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            if x - delta in bob_set:
                return [x, x - delta]
