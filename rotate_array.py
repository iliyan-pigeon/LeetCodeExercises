class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            if nums:
                number = nums.pop()
                nums.insert(0, number)
