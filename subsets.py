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


# Solution 3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with the empty subset
        result = [[]]

        # Iterate over each number in nums
        for num in nums:
            # For each existing subset, add the current number to create new subsets
            new_subsets = [curr_subset + [num] for curr_subset in result]
            # Append the new subsets to the result list
            result.extend(new_subsets)

        return result


# Solution 4
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        # Generate combinations for each possible subset size
        for k in range(n + 1):
            for subset in combinations(nums, k):
                result.append(list(subset))

        return result
      

# Solution 5
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dp(index):
            # Base case: return an empty subset when the index exceeds the list length
            if index == len(nums):
                return [[]]

            # Check the cache for previously computed subsets
            if index in memo:
                return memo[index]

            # Get subsets for the remaining elements
            next_subsets = dp(index + 1)

            # Initialize current subsets
            current_subsets = []

            # Generate subsets by adding the current element to each subset of next_subsets
            for subset in next_subsets:
                current_subsets.append(subset[:])  # Subset without current element
                current_subsets.append(subset + [nums[index]])  # Subset with current element

            # Cache the current subsets
            memo[index] = current_subsets
            return current_subsets

        memo = {}
        return dp(0)


# Solution 6
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # Start with the empty subset

        for num in nums:
            # Create new subsets by adding the current element to each existing subset
            new_subsets = []
            for existing_subset in result:
                new_subset = existing_subset + [num]
                new_subsets.append(new_subset)
            # Add the newly created subsets to the result
            result.extend(new_subsets)

        return result
        
