# Solution 1
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
# Solution 2
class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0, nums.pop())
