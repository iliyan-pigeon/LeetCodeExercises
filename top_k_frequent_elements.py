from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_count = Counter(nums)

        sorted_nums = sorted(nums_count, key=lambda x: nums_count[x], reverse=True)

        return [sorted_nums[i] for i in range(k)]
    