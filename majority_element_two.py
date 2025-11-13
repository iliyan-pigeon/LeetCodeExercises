from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)

        return [k for k, v in nums_count.items() if v > len(nums)/3]
    