from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1 << n  # 2^n subsets
        result = []

        for subset_mask in range(total_subsets):
            current_subset = []
            for i in range(n):
                # Check if the i-th bit is set in subset_mask
                if subset_mask & (1 << i):
                    current_subset.append(nums[i])
            result.append(current_subset)

        return result
      
