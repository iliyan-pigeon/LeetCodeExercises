from typing import List
from collections import defaultdict


# Solution 1
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        pairs_amount = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if k - nums[j] == nums[i] and i not in pairs_amount and j not in pairs_amount:
                    pairs_amount.extend([i, j])
                    break

        return len(pairs_amount) // 2


# Solution 2
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        count = 0

        nums.sort()

        while left != right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return count


# Solution 3
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        count = 0

        for num in nums:
            complement = k - num
            if counter[complement] > 0:
                count += 1
                counter[complement] -= 1
            else:
                counter[num] += 1

        return count
