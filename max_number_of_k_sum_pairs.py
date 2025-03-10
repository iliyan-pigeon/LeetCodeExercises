from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        pairs_amount = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if k - nums[j] == nums[i] and i not in pairs_amount and j not in pairs_amount:
                    pairs_amount.extend([i, j])
                    break

        return len(pairs_amount) // 2



a = Solution()

print(a.maxOperations([3,1,3,4,3], 6))
