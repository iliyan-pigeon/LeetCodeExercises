from collections import deque


class Solution(object):
    def rotate(self, nums, k):
        nums_queue = deque(nums)
        for i in range(k):
            number = nums_queue.pop()
            nums_queue.appendleft(number)

        nums = list(nums_queue)    

        return nums

