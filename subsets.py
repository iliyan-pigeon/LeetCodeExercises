from typing import List


# Solution 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append the current subset to the result
            result.append(path[:])
            length_nums = len(nums)
            for i in range(start, length_nums):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Move to the next element
                current = backtrack(i + 1, path)
                # Exclude nums[i] from the subset and backtrack
                path.pop()

            return path[:]

        result = []
        backtrack(0, [])
        return result


# Solution 2
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
      
