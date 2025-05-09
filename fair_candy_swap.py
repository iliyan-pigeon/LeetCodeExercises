from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        for i in aliceSizes:
            for j in bobSizes:
                if alice_total - i + j == bob_total + i - j:
                    return [i, j]
                  
