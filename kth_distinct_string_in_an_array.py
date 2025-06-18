from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        amounts = {}

        for ch in arr:
            if ch not in amounts:
                amounts[ch] = 0
            amounts[ch] += 1

        distinct_count = 0

        for key, value in amounts.items():
            if value == 1:
                distinct_count += 1

                if distinct_count == k:
                    return key
        return ""
