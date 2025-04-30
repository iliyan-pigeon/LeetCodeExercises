from typing import List


# Solution 1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if i % 2 != 0:
                result += nums[i]

        return result


# Solution 2
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr= sorted(nums)
        result=0
        for i in range (0,len(arr),2):
            result+=arr[i]
        return result


# Solution 3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
  
