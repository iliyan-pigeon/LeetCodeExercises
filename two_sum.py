# Solution 1
def twoSum(nums, target):

    for i in range(len(nums) - 1):
        if abs(nums[i]) <= abs(target):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 2
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i

        return []
