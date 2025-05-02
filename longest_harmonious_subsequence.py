from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:

        front = 0
        back = 1

        result = 0
        start = nums[front]
        nums.sort()

        while front != len(nums)-1:
            current = nums[front:back]
            filtered = [i for i in current if i == start or i-1 == start]

            if current == filtered and len(filtered) > result:
                result = len(filtered)

            elif len(current) != len(filtered) or back == len(nums):
                front += 1
                start = nums[front]

            if back != len(nums):
                back += 1

        return result
        
