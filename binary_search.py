from typing import List


# Solution 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# Solution 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        for i, v in enumerate(nums):
            if v == target:
                result = i
                break

        return result
