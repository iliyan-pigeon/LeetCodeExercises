class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if nums.count(nums[i]) > 2:
                nums.pop(i)
