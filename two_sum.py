def twoSum(nums, target):

    for i in range(len(nums) - 1):
        if abs(nums[i]) <= abs(target):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(twoSum([-1,-2,-3,-4,-5], -8))
