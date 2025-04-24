from typing import List


# Solution 1
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Solution 2
class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.arr[i + 1] = self.arr[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]
